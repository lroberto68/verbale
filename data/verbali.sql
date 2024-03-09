--
-- File generato con SQLiteStudio v3.4.4 su ven mar 8 00:38:10 2024
--
-- Codifica del testo utilizzata: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabella: Azienda
CREATE TABLE IF NOT EXISTS Azienda (IdAzi INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, DescAzienda TEXT NOT NULL);

-- Tabella: Delegato
CREATE TABLE IF NOT EXISTS Delegato (
	IdDeleg INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nome TEXT NOT NULL,
	Cognome TEXT NOT NULL,
	IdAzi INTEGER NOT NULL,
	CONSTRAINT Delegato_Azienda_FK FOREIGN KEY (IdAzi) REFERENCES Azienda(IdAzi) ON DELETE RESTRICT
);

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

-- Tabella: Logotipo
CREATE TABLE IF NOT EXISTS Logotipo (
	IdLog INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Logotipo TEXT(10) NOT NULL,
	Cifre INTEGER NOT NULL,
	CifreSottassieme INTEGER NOT NULL,
	UltimaMatricola INTEGER NOT NULL,
	FlagAnno INTEGER DEFAULT (0) NOT NULL
);

-- Tabella: Provvedimento
CREATE TABLE IF NOT EXISTS Provvedimento (
	IdProv INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	DescProvvedimento TEXT NOT NULL,
	IdAzi INTEGER NOT NULL,
	CONSTRAINT Provvedimento_Azienda_FK FOREIGN KEY (IdAzi) REFERENCES Azienda(IdAzi) ON DELETE RESTRICT
);

-- Tabella: Scheda
CREATE TABLE IF NOT EXISTS Scheda (
	IdScheda INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	IdEcr INTEGER NOT NULL,
	PriMatricola INTEGER NOT NULL,
	SecMatricola INTEGER NOT NULL,
	IdDeleg INTEGER NOT NULL,
	"Data" TEXT NOT NULL,
	CONSTRAINT Scheda_Ecr_FK FOREIGN KEY (IdEcr) REFERENCES Ecr(IdEcr) ON DELETE RESTRICT,
	CONSTRAINT Scheda_Delegato_FK FOREIGN KEY (IdDeleg) REFERENCES Delegato(IdDeleg) ON DELETE RESTRICT
);

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
