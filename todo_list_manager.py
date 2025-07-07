class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} | {status} | Due: {self.due_date} | Priority: {self.priority}"


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def list_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False

    def clear_tasks(self):
        self.tasks = []

    def is_empty(self):
        return len(self.tasks) == 0
