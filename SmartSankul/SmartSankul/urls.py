"""SmartSankul URL Configuration


"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,adminviews,staffviews,studentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.BASE,name='base'),

    #Login
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    #Admin path
    path('Admin/home',adminviews.HOME,name='admin_home'),
    path('Admin/Student/Add',adminviews.ADD_STUDENT,name='add_student'),
    path('Admin/Student/View',adminviews.VIEW_STUDENT,name='view_student'),
    path('Admin/Student/Edit/<str:id>',adminviews.EDIT_STUDENT,name='edit_student'),
    path('Admin/Student/Update',adminviews.UPDATE_STUDENT,name='update_student'),
    path('Admin/Student/Delete/<str:admin>',adminviews.DELETE_STUDENT,name='delete_student'),
    path('Admin/Course/Add',adminviews.ADD_COURSE,name='add_course'),
    path('Admin/Course/View',adminviews.VIEW_COURSE,name='view_course'),
    path('Admin/Course/Edit/<str:id>',adminviews.EDIT_COURSE,name='edit_course'),
    path('Admin/Course/Update',adminviews.UPDATE_COURSE,name='update_course'),
    path('Admin/Course/Delete/<str:id>', adminviews.DELETE_COURSE, name='delete_course'),


    path('Admin/Staff/Add',adminviews.ADD_STAFF,name='add_staff'),
    path('Admin/Staff/View', adminviews.VIEW_STAFF, name='view_staff'),
    path('Admin/Staff/Edit/<str:id>', adminviews.EDIT_STAFF, name='edit_staff'),
    path('Admin/Staff/Update',adminviews.UPDATE_STAFF,name='update_staff'),
    path('Admin/Staff/Delete/<str:admin>',adminviews.DELETE_STAFF,name='delete_staff'),

                  #Profile Path
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

                #Subject
    path('Admin/Subject/Add',adminviews.ADD_SUBJECT,name='add_subject'),
    path('Admin/Subject/View',adminviews.VIEW_SUBJECT,name='view_subject'),
    path('Admin/Subject/Edit/<str:id>', adminviews.EDIT_SUBJECT, name='edit_subject'),
    path('Admin/Subject/Update', adminviews.UPDATE_SUBJECT, name='update_subject'),
    path('Admin/Subject/Delete/<str:id>', adminviews.DELETE_SUBJECT, name='delete_subject'),

            #session
    path('Admin/Session/Add',adminviews.ADD_SESSION,name='add_session'),
    path('Admin/Session/View',adminviews.VIEW_SESSION,name='view_session'),
    path('Admin/Session/Edit/<str:id>',adminviews.EDIT_SESSION,name='edit_session'),
    path('Admin/Session/Delete/<str:id>',adminviews.DELETE_SESSION,name='delete_session'),
    path('Admin/Session/Update',adminviews.UPDATE_SESSION,name='update_session'),

    path('Admin/Staff/Send_Notification',adminviews.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Admin/Staff/save_notification',adminviews.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('Admin/Student/send_notification',adminviews.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('Admin/Student/save_notification',adminviews.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),

    path('Admin/Student/feedback',adminviews.STUDENT_FEEDBACK,name='get_student_feedback'),
    path('Admin/Student/feedback/reply/save',adminviews.REPLY_STUDENT_FEEDBACK,name='reply_student_feedback'),



    path('Admin/Staff/Leave_view',adminviews.Staff_Leave_view,name='staff_leave_view'),
    path('Admin/Staff/approve_leave/<str:id>',adminviews.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('Admin/Staff/disapprove_leave/<str:id>',adminviews.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),

    path('Admin/Student/Leave_view',adminviews.Student_Leave_view,name='student_leave_view'),
    path('Admin/Student/approve_leave/<str:id>',adminviews.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('Admin/Student/disapprove_leave/<str:id>',adminviews.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),
    path('Admin/View/Attendance',adminviews.VIEW_ATTENDANCE,name='view_attendance'),




    path('Admin/Staff/feedback',adminviews.STAFF_FEEDBACK,name='staff_feedback_reply'),
    path('Admin/Staff/feedback/save',adminviews.STAFF_FEEDBACK_SAVE,name='staff_feedback_reply_save'),



        #Staff  Url
    path('Staff/Home',staffviews.HOME,name='staff_home'),
    path('Staff/Notifications',staffviews.NOTIFICATIONS,name='notifications'),
    path('Staff/mark_as_done/<str:status>',staffviews.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),

    path('Staff/Apply_leave',staffviews.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Staff/Apply_leave_save',staffviews.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),


    path('Staff/Feedback',staffviews.STAFF_FEEDBACK,name='staff_feedback'),
    path('Staff/Feedback/Save',staffviews.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),


    path('Staff/Take_Attendance',staffviews.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Save_Attendance',staffviews.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('Staff/View_Attendance',staffviews.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),




    #Student Url

    path('Student/Home',studentviews.Home,name='student_home'),
    path('Student/Notifications',studentviews.STUDENT_NOTIFICATION,name='student_notification'),
    path('Student/mark_as_done/<str:status>',studentviews.STUDENT_NOTIFICATION_MARK_AS_DONE,
         name='student_notification_mark_as_done'),

    path('Student/feedback',studentviews.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/feedback/save',studentviews.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),

    path('Student/apply_for_leave',studentviews.STUDENT_LEAVE,name='student_leave'),
    path('Student/Leave_save',studentviews.STUDENT_LEAVE_SAVE,name='student_leave_save'),

    path('Student/View_Attendance',studentviews.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance')




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
