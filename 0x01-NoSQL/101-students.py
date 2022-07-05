#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    return mongo_collection.aggregate(
            [
                {'$project': {
                    'id': 1,
                    'name': 1,
                    'averageScore': {'$avg': {'$avg': "$topics.score"}}}},
                {'$sort': {'averageScore': -1}}
            ]
    )
