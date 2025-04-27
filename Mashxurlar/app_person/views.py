from django.shortcuts import render


famous_people = [
    {
        "name": "Albert Einstein",
        "profession": "Physicist",
        "biography": "  Albert Einstein was a German-born physicist who developed the theory of relativity, one of the pillars of modern physics."
    },
    {
        "name": "Leonardo da Vinci",
        "profession": "Artist and Inventor",
        "biography": "  Leonardo da Vinci was an Italian polymath of the Renaissance, known for masterpieces like the Mona Lisa and The Last Supper."
    },
    {
        "name": "Michael Jackson",
        "profession": "Singer and Dancer",
        "biography": "  Michael Jackson, known as the 'King of Pop', was an American singer, songwriter, and dancer who revolutionized pop music."
    },
    {
        "name": "Oprah Winfrey",
        "profession": "Television Host and Entrepreneur",
        "biography": "  Oprah Winfrey is an American talk show host, television producer, actress, author, and philanthropist, best known for The Oprah Winfrey Show."
    },
    {
        "name": "Elon Musk",
        "profession": "Entrepreneur and Engineer",
        "biography": "  Elon Musk is a business magnate and investor known for founding SpaceX, Tesla, and co-founding PayPal and Neuralink."
    },
    {
        "name": "William Shakespeare",
        
        "profession": "Playwright and Poet",
        "biography": "  William Shakespeare was an English playwright, poet, and actor, widely regarded as the greatest writer in the English language."
    },
    {
        "name": "Cristiano Ronaldo",
        "profession": "Footballer",
        "biography": "  Cristiano Ronaldo is a Portuguese professional footballer who is considered one of the greatest players of all time."
    },
    {
        "name": "Taylor Swift",
        "profession": "Singer and Songwriter",
        "biography": "  Taylor Swift is an American singer-songwriter known for narrative songs about her personal life and multiple Grammy Awards."
    },
    {
        "name": "Barack Obama",
        "profession": "Former U.S. President",
        "biography": "  Barack Obama served as the 44th president of the United States and was the first African-American to hold the office."
    },
    {
        "name": "Marie Curie",
        "profession": "Physicist and Chemist",
        "biography": "  Marie Curie was a Polish and naturalized-French physicist and chemist who conducted pioneering research on radioactivity."
    }
]


def home(request):
    return render(
        request=request,
        template_name='home.html',
        context={'name': [i['name'] for i in famous_people]},
    )

def infos(reques, pk):
    img = f'images/{pk+1}.webp'
    return render(
        request=reques,
        template_name='infos.html',
        context={'infos': famous_people[pk],
                 'pk': pk,
                 'img': img}
    )