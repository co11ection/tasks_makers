SELECT paragraph.paragraphnum, character.charname, character.speechcount FROM paragraph JOIN character ON character.charid = paragraph.charid;
