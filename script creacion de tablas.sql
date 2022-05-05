
CREATE TABLE admin (
    id_emp       NUMBER(8) NOT NULL,
    nom_emp      VARCHAR2(25) NOT NULL,
    apellido_emp VARCHAR2(25) NOT NULL,
    telefono     VARCHAR2(25) NOT NULL
);

ALTER TABLE admin ADD CONSTRAINT admin_pk PRIMARY KEY ( id_emp );

CREATE TABLE ciudad (
    id_ciudad  NUMBER(3) NOT NULL,
    nom_ciudad VARCHAR2(40) NOT NULL
);

ALTER TABLE ciudad ADD CONSTRAINT ciudad_pk PRIMARY KEY ( id_ciudad );

CREATE TABLE comuna (
    id_comuna        NUMBER(3) NOT NULL,
    nom_comuna       VARCHAR2(50) NOT NULL,
    ciudad_id_ciudad NUMBER(3) NOT NULL
);

ALTER TABLE comuna ADD CONSTRAINT comuna_pk PRIMARY KEY ( id_comuna );

CREATE TABLE detalle_horario (
    id_hor_det NUMBER(10) NOT NULL,
    fecha      DATE NOT NULL,
    hora_desde DATE NOT NULL,
    hora_hasta DATE NOT NULL
);

ALTER TABLE detalle_horario ADD CONSTRAINT detalle_horario_pk PRIMARY KEY ( id_hor_det );

CREATE TABLE direccion (
    lugar    CHAR(100) NOT NULL,
    latitud  FLOAT NOT NULL,
    longitud FLOAT NOT NULL
);

ALTER TABLE direccion ADD CONSTRAINT direccion_pk PRIMARY KEY ( lugar );

CREATE TABLE dueño (
    rut_dueño NUMBER(8) NOT NULL,
    dv        CHAR(1) NOT NULL,
    pnombre   VARCHAR2(30) NOT NULL,
    snombre   VARCHAR2(30),
    apaterno  VARCHAR2(30) NOT NULL,
    amaterno  VARCHAR2(30) NOT NULL,
    telefono  NUMBER(9)
);

ALTER TABLE dueño ADD CONSTRAINT dueño_pk PRIMARY KEY ( rut_dueño );

CREATE TABLE horario (
    id_horario         VARCHAR2(20) NOT NULL,
    puesto_id_puesto   NUMBER(7) NOT NULL,
    det_hor_id_hor_det NUMBER(10) NOT NULL
);

ALTER TABLE horario
    ADD CONSTRAINT horario_pk PRIMARY KEY ( id_horario,
                                            puesto_id_puesto,
                                            det_hor_id_hor_det );

CREATE TABLE marca (
    id_marca  NUMBER(4) NOT NULL,
    nom_marca VARCHAR2(40) NOT NULL
);

ALTER TABLE marca ADD CONSTRAINT marca_pk PRIMARY KEY ( id_marca );

CREATE TABLE modelo (
    id_modelo      NUMBER(8) NOT NULL,
    nom_modelo     VARCHAR2(50) NOT NULL,
    annio          NUMBER(4) NOT NULL,
    marca_id_marca NUMBER(4) NOT NULL
);

ALTER TABLE modelo ADD CONSTRAINT modelo_pk PRIMARY KEY ( id_modelo,
                                                          marca_id_marca );

CREATE TABLE puesto (
    id_puesto    NUMBER(7) NOT NULL,
    letra_puesto CHAR(2) NOT NULL,
    num_puesto   NUMBER(3) NOT NULL
);

ALTER TABLE puesto ADD CONSTRAINT puesto_pk PRIMARY KEY ( id_puesto );

CREATE TABLE reserva (
    id_reserva               NUMBER(13) NOT NULL,
    usr_vehiculo_pat         CHAR(8) NOT NULL,
    usuario_rut_user         NUMBER(8) NOT NULL,
    dia_reserva              NUMBER(2) NOT NULL,
    sucursal_est_id          NUMBER(3) NOT NULL,
    horar_id_hor             VARCHAR2(20) NOT NULL,
    horar_pue_id_puesto      NUMBER(7) NOT NULL,
    horar_det_hor_id_hor_det NUMBER(10) NOT NULL
);

ALTER TABLE reserva ADD CONSTRAINT relation_19_pk PRIMARY KEY ( id_reserva );

CREATE TABLE sucursal_est (
    id              NUMBER(3) NOT NULL,
    direccion_lugar CHAR(100) NOT NULL,
    nom_sucursal    VARCHAR2(30) NOT NULL,
    fono_suc        NUMBER(9) NOT NULL,
    admin_id_adm    NUMBER(8) NOT NULL
);

CREATE UNIQUE INDEX sucursal_est__idx ON
    sucursal_est (
        direccion_lugar
    ASC );

ALTER TABLE sucursal_est ADD CONSTRAINT sucursal_est_pk PRIMARY KEY ( id );

CREATE TABLE usuario (
    rut_user         NUMBER(8) NOT NULL,
    dv               CHAR(1) NOT NULL,
    vehiculo_patente CHAR(8) NOT NULL,
    comuna_id_comuna NUMBER(3) NOT NULL,
    pnombre          VARCHAR2(30) NOT NULL,
    snombre          VARCHAR2(30),
    apaterno         VARCHAR2(30) NOT NULL,
    amaterno         VARCHAR2(30) NOT NULL,
    gmail            VARCHAR2(45) NOT NULL,
    telefono         NUMBER(9)
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( rut_user,
                                                            vehiculo_patente );

CREATE TABLE vehiculo (
    patente               CHAR(8) NOT NULL,
    modelo_id_modelo      NUMBER(8) NOT NULL,
    modelo_marca_id_marca NUMBER(4) NOT NULL,
    dueño_rut_dueño       NUMBER(8) NOT NULL,
    color                 VARCHAR2(25) NOT NULL,
    num_ruedas            NUMBER(1) NOT NULL
);

ALTER TABLE vehiculo ADD CONSTRAINT vehiculo_pk PRIMARY KEY ( patente );

ALTER TABLE comuna
    ADD CONSTRAINT comuna_ciudad_fk FOREIGN KEY ( ciudad_id_ciudad )
        REFERENCES ciudad ( id_ciudad );

ALTER TABLE horario
    ADD CONSTRAINT horario_detalle_horario_fk FOREIGN KEY ( det_hor_id_hor_det )
        REFERENCES detalle_horario ( id_hor_det );

ALTER TABLE horario
    ADD CONSTRAINT horario_puesto_fk FOREIGN KEY ( puesto_id_puesto )
        REFERENCES puesto ( id_puesto );

ALTER TABLE modelo
    ADD CONSTRAINT modelo_marca_fk FOREIGN KEY ( marca_id_marca )
        REFERENCES marca ( id_marca );

ALTER TABLE reserva
    ADD CONSTRAINT relation_19_usuario_fk FOREIGN KEY ( usuario_rut_user,
                                                        usr_vehiculo_pat )
        REFERENCES usuario ( rut_user,
                             vehiculo_patente );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_horario_fk FOREIGN KEY ( horar_id_hor,
                                                    horar_pue_id_puesto,
                                                    horar_det_hor_id_hor_det )
        REFERENCES horario ( id_horario,
                             puesto_id_puesto,
                             det_hor_id_hor_det );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_sucursal_est_fk FOREIGN KEY ( sucursal_est_id )
        REFERENCES sucursal_est ( id );

ALTER TABLE sucursal_est
    ADD CONSTRAINT sucursal_est_admin_fk FOREIGN KEY ( admin_id_adm )
        REFERENCES admin ( id_emp );

ALTER TABLE sucursal_est
    ADD CONSTRAINT sucursal_est_direccion_fk FOREIGN KEY ( direccion_lugar )
        REFERENCES direccion ( lugar )
            ON DELETE CASCADE;

ALTER TABLE usuario
    ADD CONSTRAINT usuario_comuna_fk FOREIGN KEY ( comuna_id_comuna )
        REFERENCES comuna ( id_comuna );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_vehiculo_fk FOREIGN KEY ( vehiculo_patente )
        REFERENCES vehiculo ( patente )
            ON DELETE CASCADE;

ALTER TABLE vehiculo
    ADD CONSTRAINT vehiculo_dueño_fk FOREIGN KEY ( dueño_rut_dueño )
        REFERENCES dueño ( rut_dueño );

ALTER TABLE vehiculo
    ADD CONSTRAINT vehiculo_modelo_fk FOREIGN KEY ( modelo_id_modelo,
                                                    modelo_marca_id_marca )
        REFERENCES modelo ( id_modelo,
                            marca_id_marca );

CREATE OR REPLACE TRIGGER fkntm_sucursal_est BEFORE
    UPDATE OF direccion_lugar ON sucursal_est
BEGIN
    raise_application_error(-20225, 'Non Transferable FK constraint  on table SUCURSAL_EST is violated');
END;
/



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            14
-- CREATE INDEX                             1
-- ALTER TABLE                             27
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           1
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
