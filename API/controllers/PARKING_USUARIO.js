const { create } = require('../services/users/create');
const { findByUsername } = require('../services/users/find');

async function _create(user) {
    return await create(user);
}

async function _findByUsername(RUT_USER) {
    return await findByUsername(RUT_USER);
}

module.exports = {
    _create, _findByUsername
}