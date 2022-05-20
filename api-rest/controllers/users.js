const { create } = require('../services/users/create');
const { findByUsername } = require('../services/users/find');

async function _create(parking_user) {
    return await create(parking_user);
}

async function _finByUsername(rutuser) {
    return await findByUsername(rutuser);
}

module.exports = {
    _create, _finByUsername
}