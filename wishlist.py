from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import Wishlist, Comment
from forms import WishlistItemForm, EditWishlistItemForm, CommentForm
from app import db
import logging

wishlist = Blueprint('wishlist', __name__)

@wishlist.route('/wishlist')
@login_required
def view_wishlist():
    items = Wishlist.query.filter_by(user_id=current_user.id).all()
    return render_template('wishlist.html', items=items)

@wishlist.route('/wishlist/add', methods=['GET', 'POST'])
@login_required
def add_wishlist_item():
    form = WishlistItemForm()
    if form.validate_on_submit():
        try:
            new_item = Wishlist(
                item_name=form.item_name.data,
                item_url=form.item_url.data,
                price_range=form.price_range.data,
                public=form.public.data,
                notes=form.notes.data,
                user_id=current_user.id
            )
            db.session.add(new_item)
            db.session.commit()
            flash('Item added to your wishlist!', 'success')
            return redirect(url_for('wishlist.view_wishlist'))
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error adding wishlist item: {str(e)}")
            flash('An error occurred while adding the item. Please try again.', 'danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {field}: {error}", 'danger')
    
    return render_template('add_wishlist_item.html', form=form)

@wishlist.route('/wishlist/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_wishlist_item(item_id):
    item = Wishlist.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        flash('You do not have permission to remove this item.', 'danger')
        return redirect(url_for('wishlist.view_wishlist'))
    db.session.delete(item)
    db.session.commit()
    flash('Item removed from your wishlist.', 'success')
    return redirect(url_for('wishlist.view_wishlist'))

@wishlist.route('/wishlist/edit/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edit_wishlist_item(item_id):
    item = Wishlist.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        flash('You do not have permission to edit this item.', 'danger')
        return redirect(url_for('wishlist.view_wishlist'))
    
    form = EditWishlistItemForm()
    if form.validate_on_submit():
        item.item_name = form.item_name.data
        item.item_url = form.item_url.data
        item.price_range = form.price_range.data
        item.public = form.public.data
        item.notes = form.notes.data
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('wishlist.view_wishlist'))
    elif request.method == 'GET':
        form.item_name.data = item.item_name
        form.item_url.data = item.item_url
        form.price_range.data = item.price_range
        form.public.data = item.public
        form.notes.data = item.notes
    
    return render_template('edit_wishlist_item.html', form=form, item=item)

@wishlist.route('/shopping_list')
@login_required
def shopping_list():
    public_items = Wishlist.query.filter_by(public=True).filter(Wishlist.user_id != current_user.id).all()
    sorted_items = sorted(public_items, key=lambda item: item.bought)
    return render_template('shopping_list.html', items=sorted_items)

@wishlist.route('/shopping_list/mark_bought/<int:item_id>', methods=['POST'])
@login_required
def mark_bought(item_id):
    item = Wishlist.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        flash('You cannot mark your own item as bought.', 'danger')
    else:
        item.bought = True
        db.session.commit()
        flash('Item marked as bought!', 'success')
    return redirect(url_for('wishlist.shopping_list'))

@wishlist.route('/shopping_list/mark_available/<int:item_id>', methods=['POST'])
@login_required
def mark_available(item_id):
    item = Wishlist.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        flash('You cannot mark your own item as available.', 'danger')
    else:
        item.bought = False
        db.session.commit()
        flash('Item marked as available!', 'success')
    return redirect(url_for('wishlist.shopping_list'))

@wishlist.route('/shopping_list/comments/<int:item_id>', methods=['GET', 'POST'])
@login_required
def item_comments(item_id):
    item = Wishlist.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        flash('You cannot view comments on your own items.', 'warning')
        return redirect(url_for('wishlist.shopping_list'))
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, user_id=current_user.id, wishlist_item_id=item.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added.', 'success')
        return redirect(url_for('wishlist.item_comments', item_id=item.id))

    comments = Comment.query.filter_by(wishlist_item_id=item.id).order_by(Comment.created_at.desc()).all()
    return render_template('item_comments.html', item=item, form=form, comments=comments)