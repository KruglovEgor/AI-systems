%������ ���� ���������� � ������ ���������
?- element(Name, 'Dendro').
?- findall(Name, element(Name, 'Dendro'), Results).

%������ ���� ������� ���������� � �����
?- gender(Name, 'Female'), weapon(Name, 'Bow').
?- findall(Name, (gender(Name, 'Female'), weapon(Name, 'Bow')), Results), print(Results).


%�������� ����� �� ������� ������� 'Hu Tao' � 'Barbara' (�����)
?- can_have_reaction('Hu Tao', 'Barbara').

%�������� ����� �� ������� ������� 'Itto' � 'Jean' (�� �����)
?- can_have_reaction('Itto', 'Jean').

% ������ ���� ���������� ������� ����� ������� ������� � 'Ayaka' � ���
% ���� �� ������ � ��� �������
?- can_have_reaction('Ayaka', Name), from_same_region('Ayaka', Name).
?- findall(Name, (can_have_reaction('Ayaka', Name), from_same_region('Ayaka', Name)), Results), print(Results).

% ������ ���� ���������� �������� ���, ������� �� ����� ������� �������
% � ���
?- is_range(Name), element(Name, Element), not(reaction(_,'Geo', Element)).  %����� ���������� Element
?- findall(Name, (is_range(Name), element(Name, Element), not(reaction(_,'Geo', Element))), Results), print(Results). %������ Names
