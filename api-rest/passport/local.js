const LocalStrategy = require('passport-local').Strategy,
{ _finByUsername } = require('../controllers/users'),
bcrypt = require('bcrypt');

module.exports = new LocalStrategy({ session: false }, async (rutuser, password, done) => {
    try {
        const parking_user = await _finByUsername(rutuser);
        if (!parking_user) return done(null, false, 'Usuario o contraseña incorrectos');
        const match = bcrypt.compareSync(password, parking_user.password);
        if (!match) return done(null, false, 'Usuario o contraseña incorrectos');
        return done(null, {
            rutuser: parking_user.rutuser,
            id: parking_user.id,
            created_at: parking_user.created_at,
            created_at: parking_user.update_at,
            created_at: parking_user.deleted_at
        });
    } catch (e) {
        done(e);
    }
})