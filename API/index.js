// el puerto es modificable
const port = process.env.PORT || 3000,
// el puerto es modificable
express = require('express'),
app = express();
db = require('./models');
cors = require('cors'),
bodyParser = require('body-parser');

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use('auth', require('./routes/auth'));

app.listen(port, () => {
    console.log('Servidor corriendo en el puerto'+ port);
});

db.sequelize
//cambiar a true si deseas hacer cambios en la tabla ingresar tablas nuevas etc
.sync({ force: false })
//cambiar a true si deseas hacer cambios en la tabla ingresar tablas nuevas etc
.then(() => console.log('Conectado a la base de datos...'))
.catch((e) => console.log('Error falta de sexo'));


