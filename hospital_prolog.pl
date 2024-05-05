% Define symptoms for various diseases
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, headache).
symptom(flu, fatigue).

symptom(cold, runny_nose).
symptom(cold, sore_throat).
symptom(cold, sneezing).
symptom(cold, cough).

symptom(allergy, sneezing).
symptom(allergy, runny_nose).
symptom(allergy, itchy_eyes).
symptom(allergy, rash).

% Rules to determine diseases based on symptoms
has_disease(Disease, Symptoms) :-
    symptom(Disease, Symptom),
    member(Symptom, Symptoms).

% Recommendation for diseases
recommendation(flu, 'Take plenty of rest and drink fluids. You may take over-the-counter medication for fever and headache if necessary.').
recommendation(cold, 'Stay warm and drink fluids. Over-the-counter cold medications may help with symptoms.').
recommendation(allergy, 'Avoid allergens as much as possible. Antihistamines can help relieve symptoms. Consult a doctor for severe allergies.').
recommendation(_, 'It is recommended to consult a doctor for proper diagnosis and treatment.').

% Main predicate to diagnose disease and provide recommendation
diagnose(Symptoms) :-
    has_disease(Disease, Symptoms),
    write('You may have '), write(Disease), write('.'), nl,
    recommendation(Disease, Recommendation),
    write('Recommendation: '), write(Recommendation), nl.
diagnose(_) :-
    write('Unable to diagnose the disease. Please provide more symptoms or consult a doctor.'), nl.

% Example usage:
% diagnose([fever, cough, headache]). % Output: You may have flu. Recommendation: Take plenty of rest and drink fluids. You may take over-the-counter medication for fever and headache if necessary.
