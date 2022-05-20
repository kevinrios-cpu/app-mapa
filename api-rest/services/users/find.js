const db = require('../../models');

async function findByUsername(rutuser) {
    if (!rutuser) throw new Error('Nombre de usuario no dado');
    return await db.parking_user.findOne({
        where: {
            rutuser
        }
    })
}

module.exports = {
    findByUsername
}