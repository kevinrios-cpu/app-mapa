const express = require("express"),
router = express.Router(),
{ _create, _findByUsername } = require('../controllers/PARKING_USUARIO');

router.post('/signup', async(req, res) => {
    try {
        //funcionalidad para no tener usuarios duplicados
        const foundUser = await _findByUsername(req.body.RUT_USER);
        if(foundUser) {
            return res.status(400).json('El usuario ' + foundUser.RUT_USER + 'ya existe')
        }

        //aviso para cuando se cree el usuario
        const user = await _create(req, body);
        return res.status(201).json({
            status: 'succes',
            message: 'El usuario'+ user.RUT_USER + 'fue creado satisfactoriamente'
        });
    } catch (e) {
        return res.status(500).json(e.message);
    }
});

module.exports = router;