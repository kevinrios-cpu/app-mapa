var express = require("express");
var app = express();
var router = express.Router();
var bodyparser=require('body-parser');
var oracledb = require('oracledb');
//Authoriser tous les requettes cors)
var cors = require('cors');
app.use(cors());

app.use(bodyparser.json());

///Pour changer le format de la requete 
app.use(bodyparser.urlencoded({
    extended: true
}));


/// Data base ///

var connAttrs = {
    "user": "estacionamiento",
    "password": "1234",
    "connectString": "3.86.91.122/xe"
}



///// GET DIRECCION////// done
app.get('/direccion', function (req, res) {
    "use strict";

    oracledb.getConnection(connAttrs, function (err, connection) {
        if (err) {
            // Error connecting to DB
            res.set('Content-Type', 'application/json');
            res.status(500).send(JSON.stringify({
                status: 500,
                message: "Error connecting to DataBase",
                detailed_message: err.message
            }));
            return;
        }
        connection.execute("SELECT * FROM PARKING_DIRECCION", {}, {
            outFormat: oracledb.OBJECT // Return the result as Object
        }, function (err, result) {
            if (err) {
                res.set('Content-Type', 'application/json');
                res.status(500).send(JSON.stringify({
                    status: 500,
                    message: "Error getting the PARKING_DIRECCION",
                    detailed_message: err.message
                }));
            } else {
                res.header('Access-Control-Allow-Origin','*');
                res.header('Access-Control-Allow-Headers','Content-Type');
                res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS');
                res.contentType('application/json').status(200);
                res.send(JSON.stringify(result.rows));
				
            }
            // Release the connection
            connection.release(
                function (err) {
                    if (err) {
                        console.error(err.message);
                    } else {
                        console.log("GET /TablaEnviada : Conexion exitosa :D");
                    }
                });
        });
    });
});

app.get('/reserva', function (req, res) {
    "use strict";

    oracledb.getConnection(connAttrs, function (err, connection) {
        if (err) {
            // Error connecting to DB
            res.set('Content-Type', 'application/json');
            res.status(500).send(JSON.stringify({
                status: 500,
                message: "Error connecting to DataBase",
                detailed_message: err.message
            }));
            return;
        }
        connection.execute("SELECT * FROM PARKING_RESERVA", {}, {
            outFormat: oracledb.OBJECT // Return the result as Object
        }, function (err, result) {
            if (err) {
                res.set('Content-Type', 'application/json');
                res.status(500).send(JSON.stringify({
                    status: 500,
                    message: "Error getting the PARKING_RESERVA",
                    detailed_message: err.message
                }));
            } else {
                res.header('Access-Control-Allow-Origin','*');
                res.header('Access-Control-Allow-Headers','Content-Type');
                res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS');
                res.contentType('application/json').status(200);
                res.send(JSON.stringify(result.rows));
				
            }
            // Release the connection
            connection.release(
                function (err) {
                    if (err) {
                        console.error(err.message);
                    } else {
                        console.log("GET /TablaEnviada : Conexion exitosa :D");
                    }
                });
        });
    });
});

app.post('/reserva', function (req, res) {
    
    oracledb.getConnection(connAttrs, function (err, connection) {
        if (err) {
            // Error connecting to DB
            res.set('Content-Type', 'application/json');
            res.status(500).send(JSON.stringify({
                status: 500,
                message: "Error connecting to DataBase",
                detailed_message: err.message
            }));
            return;
        }
        connection.execute("INSERT INTO PARKING_RESERVA (ID_RESERVA,FECHA,HORA_DESDE,HORA_HASTA,ESTACIONAMIENTO_ID,USR_VEHICULO_PAT,ESTADO) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [req.body.ID_RESERVA, req.body.FECHA, req.body.HORA_DESDE. req.body.HORA_HASTA, req.body.ESTACIONAMIENTO_ID, req.body.USR_VEHICULO_PAT, req.body.ESTADO], {
        }, function (err, result) {
            if (err) {
                res.set('Content-Type', 'application/json');
                res.status(500).send(JSON.stringify({
                    status: 500,
                    message: "Error Post the PARKING_RESERVA",
                    detailed_message: err.message
                }));
            } else {
                res.header('Access-Control-Allow-Origin','*');
                res.header('Access-Control-Allow-Headers','Content-Type');
                res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS');
                res.contentType('application/json').status(200);
                res.send(JSON.stringify(result.rows));
				
            }
            // Release the connection
            connection.release(
                function (err) {
                    if (err) {
                        console.error(err.message);
                    } else {
                        console.log("POST /TablaEnviada : Conexion exitosa :D");
                    }
                });
        });
    });
});



app.listen(3100,function(){
  console.log("Live at Port 3100");
});