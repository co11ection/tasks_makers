SELECT chapter.chapterid, chapter.description, work.title FROM chapter JOIN work ON chapter.workid = work.workid;
