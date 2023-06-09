from flask import *
from database import init_db, db_session
from models import *
from admin import ADMIN_CODE

app = Flask(__name__)

app.secret_key = 'S4/Zdjg1sLG/knYR9i7lKg=='

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    # updating like button when the button form is submitted
    if request.method == 'POST':
            snack_id = request.form['snack']
            snack = db_session.query(Snack).filter_by(id = snack_id).first()
            snack.like_count += 1
            db_session.commit()

    # Check if the user is logged in
    user = None
    if 'username' in session:
        user = db_session.query(User).filter_by(username=session['username']).first()
        
    # gives username and snacks to home.html for future "is_admin check" 
    # and to make sure snacks are updated
    snacks = db_session.query(Snack)
    return render_template("home.html", user=user, snacks=snacks)

# replicated code of home
@app.route("/updates", methods=['GET', 'POST'])
def updates():
    
    if request.method == 'POST':
            snack_id = request.form['snack']
            snack = db_session.query(Snack).filter_by(id = snack_id).first()
            snack.like_count += 1
            db_session.commit()
    
    user = db_session.query(User).filter_by(username=session['username']).first()
    snacks = db_session.query(Snack)
    return render_template("updates.html", user=user, snacks=snacks)


@app.route("/signup", methods=['GET', 'POST'])
def signup():

    # gets information from form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        admin_code = request.form['admin_code']

        # Validate password
        if password != confirm_password:
            flash("Passwords do not match. Please try again.")
            return redirect(url_for('signup'))

        # check admin code
        if admin_code:
            if admin_code == ADMIN_CODE:
                is_admin = True
            else:
                flash("Incorrect admin code. Please try again.")
                return redirect(url_for('signup'))
        else:
            is_admin = False


        # Check if user already exists in the database
        existing_user = db_session.query(User).filter_by(username=username).first()
        if existing_user:
            flash("That username is already taken. Please choose another.")
            return redirect(url_for('signup'))

        # create a new user object and add it to the database
        new_user = User(username=username, password=password, is_admin=is_admin)
        db_session.add(new_user)
        db_session.commit()

        return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template("signup.html")
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':      
        # Render the login page
        return render_template('login.html')

    elif request.method == 'POST':
        # Get username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database and the password is correct
        user = db_session.query(User).where((User.username == username) & (User.password == password)).first()
        while user == None:
            flash("Invalid username or password")
            return render_template('login.html')
        else:
            session['username'] = username
            return redirect(url_for('home'))





            
        
    
    

@app.route("/update_snack", methods=["GET", "POST"])
def update_snack():
    
    if request.method == "POST":
        # Get the data from the form
        old_name = request.form["old-name"]
        name = request.form["name"]
        link = request.form["link"]
        image = request.form["image"]

        # Get snack to be replaced
        old_snack = db_session.query(Snack).filter_by(name=old_name).first()
        if old_snack is None:
            flash("Snack to be replaced not found")
            return redirect(url_for("update_snack"))

        

        # Update the snack
        old_snack.name = name
        old_snack.image = image
        old_snack.link = link
        old_snack.like_count = 0

        # Commit the changes to the database
        db_session.commit()

        flash("Snack updated successfully!")
        return redirect(url_for("home"))

    elif request.method == 'GET': 
        # Check if the user is an admin
        user = db_session.query(User).filter_by(username=session['username']).first()
        if not user.is_admin:
            flash("must be an admin to edit snacks")
            return redirect(url_for('home'))
        else:
            return render_template("update_snack.html")

# logoout
@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)

