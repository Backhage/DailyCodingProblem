from collections import defaultdict, deque


def find_order(course_to_prereqs):
    # Copy list values into a set for faster removal.
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}

    # Start off our to-do list with all courses without prerequisites
    todo = deque([c for c, p in course_to_prereqs.items() if not p])

    # Create a new data structure to map prereqs to successor courses.
    prereq_to_courses = defaultdict(list)
    for course, prereqs in course_to_prereqs.items():
        for prereq in prereqs:
            prereq_to_courses[prereq].append(course)

    result = []

    while todo:
        prereq = todo.popleft()
        result.append(prereq)

        # Remove this prereq from all successor courses.
        # If any course now does not have any prereqs, add it to todo.
        for c in prereq_to_courses[prereq]:
            course_to_prereqs[c].remove(prereq)
            if not course_to_prereqs[c]:
                todo.append(c)

    # Circular dependency
    if len(result) < len(course_to_prereqs):
        return None

    return result
