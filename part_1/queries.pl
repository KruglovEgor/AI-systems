%Найдем всех персонажей с дендро элементом
?- element(Name, 'Dendro').
?- findall(Name, element(Name, 'Dendro'), Results).

%Найдем всех женских персонажей с луком
?- gender(Name, 'Female'), weapon(Name, 'Bow').
?- findall(Name, (gender(Name, 'Female'), weapon(Name, 'Bow')), Results), print(Results).


%Проверим могут ли вызвать реакцию 'Hu Tao' и 'Barbara' (могут)
?- can_have_reaction('Hu Tao', 'Barbara').

%Проверим могут ли вызвать реакцию 'Itto' и 'Jean' (не могут)
?- can_have_reaction('Itto', 'Jean').

% Найдем всех персонажей которые могут вызвать реакцию с 'Ayaka' и при
% этом из одного с ней региона
?- can_have_reaction('Ayaka', Name), from_same_region('Ayaka', Name).
?- findall(Name, (can_have_reaction('Ayaka', Name), from_same_region('Ayaka', Name)), Results), print(Results).

% Найдем всех персонажей дальнего боя, которые не могут вызвать реакцию
% с гео
?- is_range(Name), element(Name, Element), not(reaction(_,'Geo', Element)).  %будет выводиться Element
?- findall(Name, (is_range(Name), element(Name, Element), not(reaction(_,'Geo', Element))), Results), print(Results). %только Names
