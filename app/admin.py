
import os

from utils.db_api.schemas import Lessons, Timetable, Teacher, TeacherRating, User

from utils.db_api.db_gino import db
from sanic import Sanic, response

from gino_admin import add_admin_panel

app = Sanic(name=__name__)
app.config["ADMIN_USER"] = "admin"
app.config["ADMIN_PASSWORD"] = "1234"

app.config["DB_HOST"] = os.environ.get("POSTGRES_HOST", "localhost")
app.config["DB_DATABASE"] = "localhost"
app.config["DB_USER"] = "postgres"
app.config["DB_PASSWORD"] = "postgres"

db.init_app(app)


@app.route("/")
async def index(request):
    return response.redirect("/admin")


current_path = os.path.dirname(os.path.abspath(__file__))


add_admin_panel(
    app,
    db,
    [User, Lessons, Timetable, Teacher, TeacherRating],
    # any Gino Admin Config params
    presets_folder=os.path.join(current_path, "csv_to_upload"),
    name="Demo Gino Admin Panel",
    route="/gino_admin_demo",
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT", 5000), debug=True)