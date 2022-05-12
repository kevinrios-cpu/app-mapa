const db = require('../../models');
const bcrypt = require('bcrypt');

async function create(user){
    if (!user.RUT_USER) throw new Error('Nombre de usuario no dado...');
    if (!user.PASSWORD) throw new Error('Contraseña no dada...');

    return await db.user.create({
        ...user,
        PASSWORD: bcrypt.hashSync(user.PASSWORD, 10)
    });
}

module.exports = {
    create
}