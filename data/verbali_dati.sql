--
-- File generato con SQLiteStudio v3.4.4 su mer mar 20 01:10:17 2024
--
-- Codifica del testo utilizzata: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabella: Azienda
CREATE TABLE IF NOT EXISTS Azienda (IdAzi INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, DescAzienda TEXT NOT NULL);
INSERT INTO Azienda (IdAzi, DescAzienda) VALUES (1, 'DITRONETWORK SRL');
INSERT INTO Azienda (IdAzi, DescAzienda) VALUES (2, 'DITRON SRL');

-- Tabella: Delegato
CREATE TABLE IF NOT EXISTS Delegato (
	IdDeleg INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nome TEXT NOT NULL,
	Cognome TEXT NOT NULL,
	IdAzi INTEGER NOT NULL,
	CONSTRAINT Delegato_Azienda_FK FOREIGN KEY (IdAzi) REFERENCES Azienda(IdAzi) ON DELETE RESTRICT
);
INSERT INTO Delegato (IdDeleg, Nome, Cognome, IdAzi) VALUES (1, 'Giorgio', ' Eutropio', 1);
INSERT INTO Delegato (IdDeleg, Nome, Cognome, IdAzi) VALUES (2, 'Roberto', ' Luongo', 2);

-- Tabella: Ecr
CREATE TABLE IF NOT EXISTS Ecr (
	IdEcr INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	CodEcr TEXT NOT NULL,
	DescEcr TEXT NOT NULL,
	IdLogotipo INTEGER NOT NULL,
	IdProvv INTEGER NOT NULL,
	StatusRec INTEGER DEFAULT (1) NOT NULL,
	CONSTRAINT Ecr_Provvedimento_FK FOREIGN KEY (IdProvv) REFERENCES Provvedimento(IdProv) ON DELETE RESTRICT,
	CONSTRAINT Ecr_Logotipo_FK FOREIGN KEY (IdLogotipo) REFERENCES Logotipo(IdLog) ON DELETE RESTRICT
);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (1, 'RTDTKN80-ST', 'RT DTK 80 ST NERO', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (2, 'RTDTKN80J-ST', 'RT DTK 80 ST J NERO', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (3, 'RTDTKB80-ST', 'RT DTK 80 ST BIANCO', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (4, 'ALLITX-V', 'ALL IN ONE 2X20', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (5, 'RTIT1G680-ST', 'RT IT1 80ST', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (6, 'LRITK', 'ECR DTK ITK LRT', 24, 2, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (7, 'LRX1W', 'ECR X1 WHITE LRT', 26, 3, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (8, 'LRIDEAL', 'ECR DITRON IDEAL RT', 27, 4, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (9, 'LRSTORE', 'ECR SWEDA STORE LRT', 31, 6, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (10, 'LRDS380', 'ECR DS 380 LRT', 31, 6, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (11, 'LRVSTORE', 'ECR VIS V-STORE LRT', 31, 6, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (12, 'LLITK-A', 'ECR DITRONETWORK ITK LRT-LC A BATTERIA WIFI', 44, 7, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (13, 'RTIT1G680R-ST', 'STAMPANTE FISCALE RT IT1 DITRONETWORK CON MPZ908T', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (14, 'RTIT1G658-ST', 'STAMPANTE TELEMATICA IT-ONE 58MM', 3, 1, 0);
INSERT INTO Ecr (IdEcr, CodEcr, DescEcr, IdLogotipo, IdProvv, StatusRec) VALUES (15, 'RTDTKB80R-ST', 'STAMP. FISCALE RT DITRONETWORK BIANCO 80 (MPZ908T)', 3, 1, 0);

-- Tabella: Logotipo
CREATE TABLE IF NOT EXISTS Logotipo (
	IdLog INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Logotipo TEXT(10) NOT NULL,
	Cifre INTEGER NOT NULL,
	CifreSottassieme INTEGER NOT NULL,
	UltimaMatricola INTEGER NOT NULL,
	FlagAnno INTEGER DEFAULT (0) NOT NULL
);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (1, '2CMXT', 6, 0, 2272, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (2, '3BIWB', 6, 0, 12605, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (3, '2CITP', 6, 0, 26390, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (4, '2CMQP', 6, 0, 66513, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (5, '2CMID', 6, 0, 10375, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (6, '2CMST', 6, 0, 9875, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (7, '2CMXS', 6, 1, 106557, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (8, '3BSDP', 6, 0, 2477, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (9, '2CMOX', 6, 0, 4215, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (10, '3BSDP', 6, 99, 990163, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (11, '2CMSG', 6, 0, 5705, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (12, '2CMPD', 6, 2, 203745, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (13, 'CCF', 6, 0, 11352, 1);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (14, '2CMSH', 6, 0, 1665, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (15, '2CMXS', 6, 2, 202932, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (16, '2CMQP', 6, 25, 252010, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (17, '2CMLK', 6, 2, 201024, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (18, '5BMFT', 6, 2, 202807, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (19, '2CMLK', 6, 0, 807, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (20, '5BIFI', 6, 2, 203309, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (21, 'AE01', 6, 0, 5109, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (22, '2CMPD', 6, 0, 960, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (23, '5BIFX', 6, 0, 503, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (24, '2CIFL', 6, 0, 20664, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (25, '2CMLK', 6, 3, 300180, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (26, '2CIXU', 6, 0, 7630, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (27, '2CIDE', 6, 0, 15484, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (28, '2CMZP', 6, 3, 301042, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (29, '2CISI', 6, 0, 3610, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (30, 'CCG', 6, 0, 3360, 1);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (31, '2CIRE', 6, 0, 13992, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (32, '2CMLK', 6, 1, 100672, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (33, '2CITP', 6, 99, 990337, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (34, '2CIDE', 6, 3, 300043, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (35, '45IPX', 6, 0, 7, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (36, '45IPX', 6, 99, 990007, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (37, '45IPA', 6, 0, 24, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (38, '45IPA', 6, 99, 990020, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (39, '2CIFL', 6, 99, 990025, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (40, '2CIXU', 6, 99, 990018, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (41, '2CIRE', 6, 99, 990015, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (42, '2CIDE', 6, 99, 990009, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (43, '2CETK', 6, 99, 990002, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (44, '2CETK', 6, 0, 1831, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (45, '2CISI', 6, 99, 990012, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (46, '5BIFI', 6, 99, 990004, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (47, '5BIFX', 6, 99, 990055, 0);
INSERT INTO Logotipo (IdLog, Logotipo, Cifre, CifreSottassieme, UltimaMatricola, FlagAnno) VALUES (48, '3BIWB', 6, 99, 990227, 0);

-- Tabella: Provvedimento
CREATE TABLE IF NOT EXISTS Provvedimento (IdProv INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, DescProvvedimento TEXT NOT NULL UNIQUE, DataProv TEXT (8) NOT NULL, VarProvvedimento TEXT, DataVariante TEXT (8), IdAzi INTEGER NOT NULL, CONSTRAINT Provvedimento_Azienda_FK FOREIGN KEY (IdAzi) REFERENCES Azienda (IdAzi) ON DELETE RESTRICT);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (1, '2023/0275536', '2023-07-06', '', '', 1);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (2, '2019/15724', '2019-01-22', '2020/15024', '2020-01-23', 1);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (3, '2019/15719', '2019-01-22', '2021/373154', '2021-12-23', 1);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (4, '2021/373215', '2021-12-23', '', '', 1);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (5, '2023/0275463', '2023-07-26', '', '', 1);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (6, '2021/191090', '2021-07-15', '2019/15734', '2019-01-22', 1);
INSERT INTO Provvedimento (IdProv, DescProvvedimento, DataProv, VarProvvedimento, DataVariante, IdAzi) VALUES (7, '2021/293944', '2021-10-29', '', '', 1);

-- Tabella: Scheda
CREATE TABLE IF NOT EXISTS Scheda (IdScheda INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, IdEcr INTEGER NOT NULL, PriMatricola INTEGER NOT NULL, SecMatricola INTEGER NOT NULL, IdDeleg INTEGER NOT NULL, Data TEXT (8) NOT NULL, CONSTRAINT Scheda_Ecr_FK FOREIGN KEY (IdEcr) REFERENCES Ecr (IdEcr) ON DELETE RESTRICT, CONSTRAINT Scheda_Delegato_FK FOREIGN KEY (IdDeleg) REFERENCES Delegato (IdDeleg) ON DELETE RESTRICT);

-- Indice: Azienda_DescAzienda_IDX
CREATE UNIQUE INDEX IF NOT EXISTS Azienda_DescAzienda_IDX ON Azienda (DescAzienda);

-- Indice: Delegato_Nome_IDX
CREATE UNIQUE INDEX IF NOT EXISTS Delegato_Nome_IDX ON Delegato (Nome,Cognome);

-- Indice: Ecr_CodEcr_IDX
CREATE INDEX IF NOT EXISTS Ecr_CodEcr_IDX ON Ecr (CodEcr);

-- Indice: Logotipo_Logotipo_IDX
CREATE UNIQUE INDEX IF NOT EXISTS Logotipo_Logotipo_IDX ON Logotipo (Logotipo,CifreSottassieme);

-- Indice: Provvedimento_DescProvvedimento_IDX
CREATE UNIQUE INDEX IF NOT EXISTS Provvedimento_DescProvvedimento_IDX ON Provvedimento (DescProvvedimento);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
