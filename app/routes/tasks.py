from flask import Blueprint,session,render_template,redirect,url_for,request
from app import db
from app.models.tasks import Tasks
tasks_bp=Blueprint('tasks',__name__)
@tasks_bp.route('/tasks')
def view_tasks():
    if 'user' in session:
        alltodo=Tasks.query.all()
        return render_template('task.html',alltodo=alltodo)
    return redirect(url_for('auth.login'))

@tasks_bp.route('/add',methods=['POST'])
def add():
    title=request.form.get("title")
    todo=Tasks(title=title,status='Pending')
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>',methods=['POST'])
def delete(task_id):
    tasks=Tasks.query.get(task_id)
    db.session.delete(tasks)
    db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>',methods=['POST'])
def toggle(task_id):
    tasks=Tasks.query.get(task_id)
    if tasks:
        if tasks.status=="Pending":
            tasks.status="In Process"
        elif tasks.status=="In Process":
            tasks.status="Completed"
        else:
            tasks.status="Pending"
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/edit/<int:task_id>',methods=['GET','POST'])
def edit(task_id):
    task=Tasks.query.get(task_id)
    if request.method=='POST':
        title=request.form.get("title")
        task.title=title
        db.session.commit()
        return redirect(url_for('tasks.view_tasks'))
    return render_template('update.html',task=task)
    