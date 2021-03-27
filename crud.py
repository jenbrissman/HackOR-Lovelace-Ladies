"""CRUD operations."""

from model import db, User, Pose, Sequence, SequenceStep, SavedSequence, SavedPose, UserPose, connect_to_db

####################################CREATE##########################################

def create_user(first_name,
                last_name,
                email,
                password_hash,
                level):
    """ Creates a new user """

    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                password_hash=password_hash,
                level=level)

    db.session.add(user)
    db.session.commit()

    return user


def create_pose(english_name,
                sanskrit_name,
                img_url):
                # instructions,
                # video_url):
    """ Creates a new pose """

    pose = Pose(english_name=english_name,
                sanskrit_name=sanskrit_name,
                img_url=img_url)
                # instructions=instructions,
                # video_url=video_url)

    db.session.add(pose)
    db.session.commit()

    return pose


def create_sequence(seq_name, level):
    """ Creates a new sequence """

    sequence = Sequence(seq_name=seq_name,
                        level=level)

    db.session.add(sequence)
    db.session.commit()

    return sequence


def create_sequence_step(step_num, pose_id, seq_id):
    """ Creates a sequence step """

    sequence_step = SequenceStep(step_num=step_num,
                                pose_id=pose_id,
                                seq_id=seq_id)

    db.session.add(sequence_step)
    db.session.commit()

    return sequence_step


def create_saved_sequence(seq_id, user_id, completed):

    saved_sequence = SavedSequence (seq_id=seq_id, 
                                    user_id=user_id,
                                    completed=completed)

    db.session.add(saved_sequence)
    db.session.commit()

    return saved_sequence                            


def create_saved_pose(pose_id, user_id):
    """ Creates a saved se. """

    saved_pose = SavedPose(
        pose_id=pose_id, user_id=user_id)

    db.session.add(saved_pose)
    db.session.commit()

    return saved_pose


####################################READ##########################################


def get_all_users():
    """Return all users."""

    return User.query.all()
    
def get_user_by_id(user_id):
    """Return a user by user ID."""

    return User.query.filter(User.user_id == user_id).first()

def get_use_by_email(email):
    """ Returns a user by their email. """

    return User.query.filter(User.email == email).first()

def get_all_poses():
    """ Returns all poses """

    return Pose.query.all()

def get_pose_by_name(pose_name):
    """Return all poses, sorted alphabetically. """
    return Pose.query.order_by(Pose.pose_name).all()

def get_pose_by_name_sanskrit(sanskrit_name):
    """ Return a pose by Sanskrit name. """

    return Pose.query.filter(Pose.sanskrit_name == sanskrit_name).first()

def get_pose_by_id(pose_id):
    """Return one pose. """

    return Pose.query.filer_by(pose_id=pose_id).one()

def get_pose_by_name_eng(english_name):
    """Return pose by English name. """

    return Pose.query.filter_by(english_name=english_name).one()

def get_user_by_email(email):
    """Return all users. """

    return User.query.filter(email=email).one()

def get_sequence_by_name(seq_name):
    """ Return a saved sequence by name. """
    return SavedSequence.query.filter(SavedSequence.seq_name = seq_nam).first()

def get_users_sequences(user_id)
    """Input user_id, return query of all user's saved sequences."""
    return SavedSequence.query.filter(SavedSequence.user_id = user_id).all()

def get_step_by_sequence()

####################################UPDATE##########################################

def update_user(user_id, first_name=None, last_name=None, new_phone=None):
    """Update user and return user."""
    
    user = db.session.query(User).get(user_id)

    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if new_phone:
        user.phone = new_phone

    db.session.commit()

    return user


####################################DELETE##########################################

def delete_user(user_id):
    """Deletes user"""

user = db.session.query(User).get(user_id)

    db.session.delete(user)
    db.session.commit()

    return f'User {user_id} is deleted.'


def delete_user_sequence(user_id, sequence_id):
    """Given user_id and sequence_id, deletes relationship from database."""
    
    unwanted_sequence = UserSequence.query.filter(UserSequence.user_id == user_id, UserSequence.sequence_id == sequence_id).one()
    db.session.delete(unwanted_sequence)
    db.session.commit() 



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
