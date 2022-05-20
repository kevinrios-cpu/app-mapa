const db = require('../../models');
const bcrypt = require('bcrypt');

async function create(parking_user) {
    if (!parking_user.rutuser) throw new Error('Nombre de usuario no dado...');
    if (!parking_user.password) throw new Error('Contraseña no dada...');

    return await db.parking_user.create({
        ...parking_user,
        password: bcrypt.hashSync(parking_user.password, 10)
    });
}

module.exports = {
    create
}