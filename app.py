
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, Identity, identity_changed, AnonymousIdentity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configurar Flask-Principal
principals = Principal(app)

# Definición de roles
admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))
usuario_permission = Permission(RoleNeed('usuario'))

# Usuarios simulados en memoria
usuarios = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "rol": "admin"
    },
    "editor": {
        "password": generate_password_hash("editor123"),
        "rol": "editor"
    },
    "usuario": {
        "password": generate_password_hash("usuario123"),
        "rol": "usuario"
    }
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.rol = usuarios[username]["rol"]

@login_manager.user_loader
def load_user(user_id):
    if user_id in usuarios:
        return User(user_id)
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if not hasattr(current_user, 'id'):
        return
    role = usuarios.get(current_user.id, {}).get('rol')
    if role:
        identity.provides.add(RoleNeed(role))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and check_password_hash(usuarios[username]['password'], password):
            user = User(username)
            login_user(user)
            identity_changed.send(app, identity=Identity(user.id))
            flash('Bienvenido, {}'.format(username), 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.id, rol=usuarios[current_user.id]["rol"])

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return render_template('admin.html')

@app.route('/editor')
@login_required
@editor_permission.require(http_exception=403)
def editor():
    return render_template('editor.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('login'))

@app.errorhandler(403)
def acceso_denegado(e):
    return render_template('denegado.html'), 403

if __name__ == '__main__':
    app.run(debug=True)
