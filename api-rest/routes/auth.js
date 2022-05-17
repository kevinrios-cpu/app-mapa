const express = require('express'),
router = express.Router(),
{ _create } = require('../controllers/users');

router.post('/signup', async(req, res) =>{
    try{
        const parking_user = await _create(req.body);
        return res.status(201).json({
            status: 'success',
            message: 'El usuario ' + parking_user.rutuser + ' fue creado satisfactoriamente...'
        })
    } catch (e) {
        return res.status(500).json(e.message);
    }
});

module.exports = router;