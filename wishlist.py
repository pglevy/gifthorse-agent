from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import Wishlist, User
from forms import WishlistItemForm, EditWishlistItemForm
from app import db

wishlist = Blueprint('wishlist', __name__)

@wishlist.route('/wishlist')
@login_required
def view_wishlist():
    items = current_user.wishlist_items.all()
    return render_template('wishlist.html', items=items)

@wishlist.route('/wishlist/add', methods=['GET', 'POST'])
@login_required
def add_wishlist_item():
    form = WishlistItemForm()
    if form.validate_on_submit():
        new_item = Wishlist(
            item_name=form.item_name.data,
            item_url=form.item_url.data,
            price_range=form.price_range.data,
            public=form.public.data,
            user_id=current_user.id
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Item added to your wishlist!', 'success')
        return redirect(url_for('wishlist.view_wishlist'))
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
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('wishlist.view_wishlist'))
    elif request.method == 'GET':
        form.item_name.data = item.item_name
        form.item_url.data = item.item_url
        form.price_range.data = item.price_range
        form.public.data = item.public
    
    return render_template('edit_wishlist_item.html', form=form, item=item)

@wishlist.route('/shopping_list')
@login_required
def shopping_list():
    public_items = Wishlist.query.filter_by(public=True).filter(Wishlist.user_id != current_user.id).all()
    return render_template('shopping_list.html', items=public_items)
