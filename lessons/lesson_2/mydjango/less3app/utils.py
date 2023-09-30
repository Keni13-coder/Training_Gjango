from .models import Post, Author,Comments
from random import choices

TEXT = '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure rerum mollitia fuga at corporis, doloribus itaque eligendi assumenda obcaecati possimus error, atque pariatur? Perferendis id pariatur dolorum. Magni, nemo assumenda.
Harum, reprehenderit nam laboriosam odit repellat dolorum inventore ullam blanditiis repudiandae. Quidem aliquid nobis cum, facilis magni tempora dolorem necessitatibus sequi aliquam veniam, autem obcaecati reprehenderit. Perspiciatis culpa facilis voluptas.
Alias consequatur, commodi doloremque at fugit porro quasi unde officiis laborum soluta totam nostrum sint aut quod eius enim impedit, minus reprehenderit. Illum dignissimos consequuntur sit dolor tempore. Rerum, excepturi?
Nostrum aliquam odio pariatur recusandae unde, expedita ut delectus fuga sed. Accusamus molestias rem quos repudiandae, error numquam officiis ad voluptate maiores a! Placeat quis tempora labore corporis ad doloribus?
A fuga fugit unde? Quibusdam deserunt ab ea! Nostrum facilis magni velit beatae totam excepturi possimus ratione officia minus reprehenderit eius quis, ad a, perferendis dolorum incidunt minima voluptatem sunt!
Id nam rerum facilis distinctio, non nesciunt aliquid provident odio ipsum quisquam asperiores laborum quidem, fugit modi maiores error nulla mollitia. Quo ullam vel quos vero rem, repellendus ut numquam!
Sed dignissimos sequi dolorem distinctio obcaecati dolor possimus aspernatur et debitis quisquam nam vel dolores fugiat temporibus vero error, doloremque ducimus veritatis quasi laudantium. Pariatur nobis accusantium maiores beatae. Vel.
A architecto alias qui, saepe cum temporibus sequi obcaecati, accusantium aut quod debitis unde culpa. Eius dolores perspiciatis adipisci a reprehenderit, sed, ratione natus quo eos ipsum illo modi amet.
Pariatur nisi animi facilis eligendi illum accusantium tenetur repellendus minus quia aliquid quibusdam reiciendis iure nihil ratione numquam sequi, maxime voluptatem optio asperiores placeat nobis dolor alias? Asperiores, voluptas commodi.
Ipsam molestias atque illum. Nihil neque asperiores cumque est, expedita sit sed quae vero consectetur magnam aliquid aliquam fugit quam excepturi praesentium rem earum dolor obcaecati minima, eius doloremque cupiditate.
Culpa voluptas perspiciatis nisi, repellat minima, vero sequi repudiandae provident accusamus animi ab placeat, nulla nostrum veritatis molestias asperiores velit! Quis saepe adipisci possimus. Adipisci iusto recusandae harum distinctio qui!
Tempore ea debitis ipsa officia. Voluptas deserunt architecto sed nihil perspiciatis cum consectetur quia! Reprehenderit, quam vitae. Ipsa, a magni ea, hic porro maxime omnis voluptatem vitae ab fugit officiis.
Voluptatem, illum? Consectetur cupiditate sapiente voluptatibus culpa, maxime dignissimos, quisquam enim odit veritatis voluptas dolorem exercitationem, magnam omnis numquam aliquid dolore velit sit! Laudantium voluptatum cum expedita excepturi perferendis eligendi.
Corrupti, quasi dolore maiores repellendus labore ab voluptate distinctio sapiente placeat? Officia, ipsum necessitatibus laudantium perspiciatis maxime nihil fugit minima aspernatur dolorum sit saepe reprehenderit tempore dolore dignissimos. Porro, omnis.
Quia blanditiis accusamus, perferendis quo eveniet eum omnis earum aut ad aliquid, quasi amet quidem doloribus provident odio non sint dolorum incidunt ullam tempore eaque atque culpa! Eveniet, iusto suscipit.'''

def create_all():
    text = TEXT.split()
    COUNT = 10
    for i in range(1, COUNT + 1):
        author = Author(name=f'Author_{i}',
                        email=f'email{i}@mail.ru',
                        second_name=f'Second_name{i}',
                        biography=f'biography{i}')
        author.save()
        for j in range(1, COUNT + 1):
            post = Post(title=f'Title-{j}',
                        content=' '.join(choices(text, k=64)),
                        author=author,
                        category=f'category-{j}'
                        )
            post.save()