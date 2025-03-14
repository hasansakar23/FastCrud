from fastapi import FastAPI,Body

app = FastAPI()

courses_db = [
    {'id': '1', 'instructor': 'Atil', 'title': 'Python','category':'Development'},
    {'id': '2', 'instructor': 'Ahmet', 'title': 'Java', 'category': 'Development'},
    {'id': '3', 'instructor': 'Atil', 'title': 'Jenkins', 'category': 'Devops'},
    {'id': '4', 'instructor': 'Zeynep', 'title': 'Kubernetes', 'category': 'Devops'},
    {'id': '5', 'instructor': 'Fatma', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': '6', 'instructor': 'Atlas', 'title': 'Deep Learning', 'category': 'AI'}
]

@app.get("/hello")
async def hello_world():
    return {"message": "Hello World"}
@app.get("/courses")
async def get_all_courses():
    return courses_db
@app.get("/courses/{course_title}")
async def get_course(course_title: str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():
            return course

@app.get("/courses/{course_id}")
async def get_course(course_id: str):
    for course in courses_db:
        if course.get('id').casefold() == course_id.casefold():
            return course

@app.get("/courses/byid/{course_id}")
async def get_course(course_id: str):
    for course in courses_db:
        if course.get('id').casefold() == course_id.casefold():
            return course

@app.get("/courses/")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/byinstructor/")
async def get_by_courses_by_instructor_path(instructor: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('instructor').casefold() == instructor.casefold():
            courses_to_return.append(course)

    return courses_to_return

@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):

    course_to_return=[]
    for course in courses_db:
        if(course.get('instructor').casefold() == course_instructor.casefold()
        and course.get('category').casefold() == category.casefold()):
            course_to_return.append(course)
            return course_to_return

@app.post("/courses/create_course")
async def create_a_course(new_course=Body()):
    courses_db.append(new_course)

@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for i in range (len(courses_db)):
        if courses_db[i].get('id').casefold() == updated_course.get('id').casefold():
            courses_db[i] = updated_course

@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id : int):
    for i in range(len(courses_db)):
        if courses_db[i].get('id').casefold() == course_id.casefold():
            courses_db.pop(i)
            break