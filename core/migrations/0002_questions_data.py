from django.db import migrations

def create_questions(apps, schema_editor):
    Question = apps.get_model('core', 'Question')
    QuestionStat = apps.get_model('core', 'QuestionStat')
    
    questions_data = [
        # Pergunta 1
        {
            'text': 'Sobre o objetivo principal do Marco Civil da Internet no Brasil, qual alternativa melhor o descreve?',
            'option_a': 'Criar crimes específicos de fraude bancária eletrônica',
            'option_b': 'Definir princípios, garantias, direitos e deveres para o uso da internet no país',
            'option_c': 'Regulamentar exclusivamente redes sociais estrangeiras',
            'option_d': 'Tratar apenas da proteção de dados de crianças',
            'correct_option': 'B', 'difficulty': 'F', 'points': 1
        },
        # Pergunta 2
        {
            'text': 'Qual dos direitos abaixo é expressamente protegido pelo Marco Civil em relação ao usuário de internet?',
            'option_a': 'Liberdade de expressão no ambiente online, respeitada a legislação',
            'option_b': 'Direito irrestrito ao anonimato em qualquer situação',
            'option_c': 'Isenção de responsabilidade por qualquer conteúdo publicado',
            'option_d': 'Acesso gratuito obrigatório a todos os sites',
            'correct_option': 'A', 'difficulty': 'F', 'points': 1
        },
        # ... (adicione todas as 20 aqui, seguindo o mesmo padrão)
        # Pergunta 20
        {
            'text': 'Em relação ao tratamento de dados de crianças e adolescentes, a LGPD estabelece que:',
            'option_a': 'Não há regras específicas; aplicam-se apenas normas gerais',
            'option_b': 'O tratamento deve considerar o melhor interesse da criança ou do adolescente',
            'option_c': 'O consentimento dos responsáveis nunca é necessário',
            'option_d': 'O tratamento de dados de menores é sempre proibido, em qualquer hipótese',
            'correct_option': 'B', 'difficulty': 'F', 'points': 1
        }
    ]
    
    for data in questions_data:
        question = Question.objects.create(**data)
        QuestionStat.objects.get_or_create(question=question)

class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]  # ajuste conforme sua última migração
    
    operations = [migrations.RunPython(create_questions)]
