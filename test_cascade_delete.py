from app import create_app, db
from models import User, Wishlist, Comment

def test_cascade_delete():
    app = create_app()
    with app.app_context():
        # Create a test user
        user = User(email='test@example.com', name='Test User')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

        # Create a wishlist item
        wishlist_item = Wishlist(user_id=user.id, item_name='Test Item', price_range='medium')
        db.session.add(wishlist_item)
        db.session.commit()

        # Create some comments for the wishlist item
        comment1 = Comment(content='Comment 1', user_id=user.id, wishlist_item_id=wishlist_item.id)
        comment2 = Comment(content='Comment 2', user_id=user.id, wishlist_item_id=wishlist_item.id)
        db.session.add(comment1)
        db.session.add(comment2)
        db.session.commit()

        # Verify that the comments exist
        comments = Comment.query.filter_by(wishlist_item_id=wishlist_item.id).all()
        print(f"Number of comments before delete: {len(comments)}")

        # Delete the wishlist item
        db.session.delete(wishlist_item)
        db.session.commit()

        # Verify that the comments have been deleted
        comments = Comment.query.filter_by(wishlist_item_id=wishlist_item.id).all()
        print(f"Number of comments after delete: {len(comments)}")

        # Clean up
        db.session.delete(user)
        db.session.commit()

if __name__ == '__main__':
    test_cascade_delete()
