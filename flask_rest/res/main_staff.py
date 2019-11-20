from flask import Blueprint, render_template, request, session, abort
from werkzeug.utils import redirect

from staff.staff_list import staff_list
from staff.form_staff import StaffForm
staff = Blueprint('staff', __name__, template_folder='templates', static_folder='static')


@staff.route('/staff/<name>')
def get_staff(name):
    print(name)
    if name is not '#':
        count = 0
        for i in staff_list:
            if i['name'] == name:
                staff_list.pop(count)
            count += 1
    return render_template("staff.html", list=staff_list)


@staff.route('/info_staff/<name>')
def get_info_staff(name):
    for i in staff_list:
        if i['name'] == name:
            return render_template("info_staff.html", list=i)


@staff.route('/add_staff', methods=['GET', 'POST'])
def get_add_staff():
    form = StaffForm()
    coint = 0
    if request.query_string:
        for i in staff_list:
            if i['passportID'] == request.args.get('edit'):
                data = {
                    'name': form.name.data,
                    'passportID': form.passportID.data,
                    'position': form.position.data,
                    'salary': form.salary.data
                }
                staff_list.pop(coint)
                staff_list.insert(coint, data)
            coint += 1

    if request.method == "POST":
        if form.validate_on_submit():
            data = {
                'name': form.name.data,
                'passportID': form.passportID.data,
                'position': form.position.data,
                'salary': form.salary.data
            }
            staff_list.append(data)
            return redirect('/staff')
    return render_template("add_staff.html", title=StaffForm, form=form)


