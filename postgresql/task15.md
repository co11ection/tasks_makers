SELECT paragraph.paragraphnum, work.title, work.year FROM paragraph JOIN work ON paragraph.workid = work.workid;
