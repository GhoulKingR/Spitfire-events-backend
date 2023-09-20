from flask import jsonify, Blueprint, request
from Event.models import Users, Groups, UserGroups

groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@groups.route("/")
def get_active_signals():
    return

@groups.route("/<groupId>/members/<userId>",methods=["POST"])
def add_user_to_group(groupId, userId):
    if request.method=='POST':
        # Handle POST Request here
        group_id = groupId
        user_id = userId
        user = Users.query.get(user_id)
        if user != None:
            group = Groups.query.get(group_id)
            add_user = UserGroups(user_id=user, group_id=group)
            # print(add_user)
            UserGroups.insert(add_user)
            return jsonify({"success":True, "id":add_user.id, "message":"User added to Group"}), 201
        else:
            return jsonify({"success": False, "message":"User not found"}), 404
    return jsonify({"success": False, "message":"Method not allowed"}), 405