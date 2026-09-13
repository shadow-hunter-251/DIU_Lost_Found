from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import ItemMatch


def build_item_text(item):
    title = item.title or ''
    description = item.description or ''
    location = item.location or ''

    category = ''

    if item.category:
        category = item.category.name

    return f'{title} {title} {description} {location} {category}'


def calculate_similarity(item1, item2):

    text1 = build_item_text(item1)
    text2 = build_item_text(item2)

    vectorizer = TfidfVectorizer(
        stop_words='english'
    )

    vectors = vectorizer.fit_transform([
        text1,
        text2
    ])

    score = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(score * 100, 2)

from items.models import Item


def find_potential_matches(item, limit=5):

    if item.item_type == 'LOST':
        opposite_type = 'FOUND'
    else:
        opposite_type = 'LOST'

    opposite_items = Item.objects.filter(
        item_type=opposite_type,
        status='ACTIVE'
    ).select_related('category')

    matches = []

    for other_item in opposite_items:

        if item.item_type == 'LOST':
            lost_item = item
            found_item = other_item
        else:
            lost_item = other_item
            found_item = item

        score = calculate_similarity(
            lost_item,
            found_item
        )

        if score >= 25:

            ItemMatch.objects.update_or_create(
                lost_item=lost_item,
                found_item=found_item,
                defaults={
                    'score': score
                }
            )

            matches.append({
                'item': other_item,
                'score': score
            })

    matches.sort(
        key=lambda x: x['score'],
        reverse=True
    )

    return matches[:limit]