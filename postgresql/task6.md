SELECT character.charname, character.speechcount, work.title FROM character JOIN character_work ON character_work.charid = character.charid JOIN work ON character_work.workid = work.workid;
