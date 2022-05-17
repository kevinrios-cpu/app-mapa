const Sequelize = require('sequelize-oracle');

module.exports = (sequelize, DataType) => {
    return sequelize.define('parking_user', {
        id: {
            type: Sequelize.INTEGER,
            autoIncrement: true,
            primaryKey: true
        },
        rutuser: {
            type: Sequelize.STRING,
            required: true,
            allowNull: false,
            len: [6, 20]
            
        },
        password: {
            type: Sequelize.STRING,
            required: true,
            allowNull: false,
            len: [8, 100]
            
        }

    }, {
        underscored: true,
        paranoid: true
    })
}