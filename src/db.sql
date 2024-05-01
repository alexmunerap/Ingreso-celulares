CREATE TABLE celulares(id Serial, marca text, modelo text, diagnostico text, nombre text, cedula text, telefono text );

INSERT INTO celulares(marca, modelo, diagnostico, nombre, cedula, telefono) VALUES
    ('huawei', 'y9 prime', 'no carga', 'luz pelaez', '43167284', '3146619276');

INSERT INTO celulares(marca, modelo, diagnostico, nombre, cedula, telefono) VALUES
    ('samsung', 's23 ultra', 'display malo');

select * from celulares;