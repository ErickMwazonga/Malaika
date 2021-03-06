# coding=utf-8
doctor_specialities = [
    'Anesthesiologists‎','Cardiologists‎','Coroners‎','Dentists‎','Dermatologists‎',
    'Diabetologists‎','Emergencyphysicians‎','Endocrinologists‎','Euthanasia doctors',
    'Gastroenterologists‎','Generalpractitioners‎','Gynaecologists‎','Hematologists‎',
    'Hygienists‎','Immunologists‎','Internists‎','Leprologists‎','Militaryphysicians‎',
    'Nephrologists‎','Neurologists‎','Neurosurgeons‎','Nuclearmedicinephysicians',
    'Obstetricians‎','Oncologists‎','Ophthalmologists‎','Orthopaedists‎',
    'Osteopathicphysicians‎','Otolaryngologists‎','Paleopathologists‎',
    'Parasitologists‎','Pathologists‎','Pediatricians‎','Phthisiatrists',
    'Podiatrists‎','Psychiatrists‎','Pulmonologists‎','Radiologists‎',
    'Rheumatologists‎','Serologists‎','Surgeons‎','Teamphysicians‎','Toxicologists‎',
    'Urologists‎','Venereologists‎']

nurse_specialities = [
    'Ambulatory care nursing','Advanced practice nursing','Burn nursing',
    'Camp nursing','Cardiac nursing','Cardiac catheter laboratory nursing',
    'Medical case management','Community health nursing','Correctional nursing',
    'Critical care nursing','Emergency and trauma nursing',
    'Environmental health nursing','Faith community nursing','Flight nursing',
    'Forensic nursing','Gastroenterology nursing',
    'Genetics nursing','Geriatric nursing','Health visiting','Holistic nursing',
    'Home health nursing','Hospice and palliative care nursing',
    'Hyperbaric nursing','Immunology and allergy nursing',
    'Intravenous therapy nursing', 'Infection control nursing',
    'Infectious disease nursing','Legal nursing',
    'Maternal-child nursing','Medical-surgical nursing',
    'Mental health or psychiatric nursing','Midwifery',
    'Military and uniformed services nursing','Neonatal nursing',
    'Neurosurgical nursing','Nursing informatics','Nursing management',
    'Nursing research','Obstetrical nursing','Occupational health nursing',
    'Oncology nursing','Orthopaedic nursing','Ostomy nursing',
    'Pediatric nursing','Perianesthesia nursing','Perioperative nursing',
    'Private duty nursing','Psychiatric or mental health nursing',
    'Public health nursing','Pulmonary nursing','Quality improvement',
    'Radiology nursing','Rehabilitation nursing','Renal nursing',
    'School nursing','Space nursing','Sub-acute nursing',
    'Substance abuse nursing','Surgical nursing','Telenursing',
    'Telephone triage nursing','Transplantation nursing','Travel nursing',
    'Urology nursing','Utilization management','Wound care']

meds = [
    'Abilify','Aciphex','Actonel','Actoplus MET','Actos','Adacel','Adderall XR',
    'Advair Diskus','Aggrenox','Aloxi','Amphetamine Salts ER','Alimta',
    'AndroGel','Angiomax','Aranesp','Asacol','Atorvastatin Calcium','Atripla',
    'Avapro','Avastin','Avelox','Avodart','Avonex','Benicar','Benicar HCT',
    'Betaseron','Boniva','Budesonide','Byetta','Bystolic','Celebrex','Chantix',
    'Cialis','Colcrys','Combivent','Concerta','Copaxone','Crestor','Cubicin',
    'Cymbalta','Detrol LA','Dexilant','Diovan','Diovan HCT','Donepezil HCl',
    'Effexor XR','Eloxatin','Enbrel','Epogen','Epzicom','Erbitux','Evista',
    'Exelon','Exforge','Fentanyl','Flomax','Flovent HFA','Fluticasone Propionate',
    'Focalin XR','Forteo','Gammagard Liquid','Gamunex-C','Gardasil','Geodon',
    'Gilenya','Gleevec','Herceptin','Humalog','Humalog Kwikpen','Humira',
    'Incivek','Invega','Invega Sustenna','Isentress','Janumet','Januvia',
    'Kaletra','Lamictal','Lantus','Lantus Solostar','Levaquin','Levemir',
    'Lexapro','Lexiscan','Lidoderm','Lialda','Lipitor','Loestrin 24 FE',
    'Lotrel','Lovaza','Lovenox','Lucentis','Lumigan','Lunesta','Lyrica',
    'Methylphenidate ER','Metoprolol Succinate','Mirena','Namenda','Nasonex',
    'Neulasta','Neupogen','Nexium','Niaspan','NovoLog','Norvir','NovoSeven RT',
    'Nuvaring','Nutropin AQ','Opana ER','Orencia','Ortho Tri-Cyclen Lo',
    'Oxycontin','Pegasys','Plavix','Pneumovax 23','Pradaxa','Premarin',
    'Prevnar 13','Prezista','Pristiq','Privigen','Procrit','Proair HFA',
    'Prograf','Provigil','Pulmozyme','Rebif','Reclast','Remicade','Renvela',
    'Restasis','Revlimid','Reyataz','Risperdal Consta','Rituxan',
    'Sandostatin LAR','Sensipar','Seroquel','Seroquel XR','Singulair','Solodyn',
    'Spiriva Handihaler','Stelara','Strattera','Suboxone','Symbicort','Synagis',
    'Synthroid','Taxotere','Tarceva','Temodar','Travatan Z','Treanda','Tricor',
    'Trilipix','Truvada','Tysabri','Varivax','Velcade','Venlafaxine HCl ER',
    'Ventolin HFA','VESIcare','Viagra','Victoza','Viread','Vytorin','Vyvanse',
    'Welchol','Xeloda','Xgeva','Xifaxan','Xolair','Xopenex','Yervoy','Zetia',
    'Zometa','Zostavax','Zosyn','Zyprexa','Zyprexa Zydis','Zyvox']

vaccines = [
    'Adenovirus Type 4 and Type 7 Vaccine,','Anthrax Vaccine','BCG',
    'Diphtheria & Tetanus Toxoids','Poliovirus Vaccine Combined',
    'Diphtheria and Tetanus Toxoids and Acellular Pertussis and Poliovirus Vaccine',
    'Haemophilus b Conjugate','Hepatitis A Vaccine',
    'Hepatitis A and Hepatitis B (Recombinant) Vaccine',
    'Hepatitis B Vaccine (Recombinant)',
    'Human Papillomavirus Quadrivalent (Types 6, 11, 16, 18) Vaccine, Recombinant',
    'Human Papillomavirus Bivalent (Types 16, 18) Vaccine, Recombinant',
    'Influenza A (H1N1) 2009 Monovalent Vaccine',
    'Influenza Virus Vaccine, H5N1 (for National Stockpile)',
    'Influenza Vaccine,, Intranasal','Influenza Virus Vaccine',
    'Influenza Vaccine (Trivalent)','Influenza Vaccine, Intranasal',
    'Influenza Virus Vaccine ','Japanese Encephalitis Virus Vaccine',
    'Japanese Encephalitis Virus Vaccine ','Measles Virus Vaccine',
    'Measles and Mumps Virus Vaccine','Measles, Mumps, and Rubella Virus Vaccine',
    'Measles, Mumps, Rubella and Varicella Virus Vaccine',
    'Meningococcal','Mumps Virus Vaccine','Plague Vaccine',
    'Pneumococcal Vaccine, Polyvalent','Pneumococcal 7-valent Conjugate Vaccine',
    'Pneumococcal 13-valent Conjugate Vaccine','Poliovirus Vaccine (Human Diploid Cell)',
    'Poliovirus Vaccine (Monkey Kidney Cell)','Rabies Vaccine',
    'Rotavirus Vaccine','Rotavirus Vaccine Pentavalent',
    'Rubella Virus Vaccine','Smallpox (Vaccinia) Vaccine',
    'Tetanus & Diphtheria Toxoids for Adult Use','Tetanus Toxoid',
    'Tetanus Toxoid, Reduced Diphtheria Toxoid and Acellular Pertussis Vaccine',
    'Typhoid Vaccine Ty21a','Typhoid Vi Polysaccharide Vaccine',
    'Varicella Virus Vaccine','Yellow Fever Vaccine','Zoster Vaccine']

departments = [
    'Acute assessment unit','Coronary care unit','Emergency department',
    'Geriatric intensive-care unit','Intensive-care unit',
    'Neonatal intensive care unit','On-call room','Operating room',
    'Pediatric intensive care unit','McKenzie method','Physical therapy',
    'Post-anesthesia care unit','Psychiatric hospital',
    'Release of information department','Urgent care']
