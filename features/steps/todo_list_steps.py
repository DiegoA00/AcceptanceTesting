from behave import given, when, then
from todo_list_manager import ToDoListManager

@given('the to-do list is empty')
def step_impl(context):
    context.manager = ToDoListManager()

@when('the user adds a task "{title}"')
def step_impl(context, title):
    context.manager.add_task(title, "desc", "tomorrow", "Medium")

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.manager.list_tasks()]
    assert title in titles

@given('the to-do list contains tasks:')
def step_impl(context):
    context.manager = ToDoListManager()
    for row in context.table:
        context.manager.add_task(row['Task'], "desc", "tomorrow", "Medium")

@given('the to-do list contains tasks with status:')
def step_impl(context):
    context.manager = ToDoListManager()
    for row in context.table:
        context.manager.add_task(row['Task'], "desc", "tomorrow", "Medium")
        if row['Status'] == 'Completed':
            context.manager.mark_completed(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = context.manager.list_tasks()

@then('the output should contain:')
def step_impl(context):
    titles = [task.title for task in context.listed_tasks]
    for row in context.table:
        assert row['Task'] in titles

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    assert context.manager.mark_completed(title)

@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    for task in context.manager.list_tasks():
        if task.title == title:
            assert task.completed
            return
    assert False, "Task not found"

@when('the user clears the to-do list')
def step_impl(context):
    context.manager.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert context.manager.is_empty()
