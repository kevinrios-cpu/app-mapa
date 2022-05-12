const Sequelize = require('sequelize-oracle');

module.exports = (sequelize, DataTypes) => {
    return sequelize.define('PARKING_USUARIO', {
        id: {
            type: Sequelize.INTEGER,
            autoIncrement: true,
            PrimaryKey: true
        },
        DV: {
            type:Sequelize.STRING,
            required: true,
            allowNull: false,
            PrimaryKey: true,
            len: [1]
        },
        RUT_USER: {
            type:Sequelize.STRING,
            required: true,
            allowNull: false,
            PrimaryKey: true,
            len: [6, 20]
        },
        PASSWORD: {
            type:Sequelize.STRING,
            required: true,
            allowNull: false,
            len: [8, 100]
        },
        

    }, {
        underscored: true,
        paranoid: true
    })
}