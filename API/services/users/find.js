const db = require('../../models');

async function findByUsername(RUT_USER) {
    if (!RUT_USER) throw new Error('Nombre de usuario no dado');
    return await db.user.findOne({
        where: {
            RUT_USER
        }
    });
}

module.exports = {
    findByUsername
}