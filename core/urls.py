from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<rfid_antenna>\d+)/$', views.home, name='home'),
	
	url(r'^(?i).*Competitions/$', views.CompetitionsDisplay),
	url(r'^(?i).*CompetitionNew/$', views.CompetitionNew),
	url(r'^(?i).*CompetitionCopy/(?P<competitionId>\d+)/$', views.CompetitionCopy),
	url(r'^(?i).*CompetitionEdit/(?P<competitionId>\d+)/$', views.CompetitionEdit),
	url(r'^(?i).*CompetitionDelete/(?P<competitionId>\d+)/$', views.CompetitionDelete),
	url(r'^(?i).*CompetitionDashboard/(?P<competitionId>\d+)/$', views.CompetitionDashboard),
	url(r'^(?i).*StartLists/(?P<competitionId>\d+)/$', views.StartLists),
	url(r'^(?i).*StartList/(?P<eventId>\d+)/$', views.StartList),
	
	url(r'^(?i).*ParticipantScan/(?P<competitionId>\d+)/$', views.ParticipantScan),
	url(r'^(?i).*ParticipantRfidScan/(?P<competitionId>\d+)/$', views.ParticipantRfidScan),
	url(r'^(?i).*ParticipantRfidScan/(?P<competitionId>\d+)/(?P<autoSubmit>\d+)/$', views.ParticipantRfidScan),
	
	url(r'^(?i).*CategoryNumbers/(?P<competitionId>\d+)/$', views.CategoryNumbersDisplay),
	url(r'^(?i).*CategoryNumbersNew/(?P<competitionId>\d+)/$', views.CategoryNumbersNew),
	url(r'^(?i).*CategoryNumbersEdit/(?P<categoryNumbersId>\d+)/$', views.CategoryNumbersEdit),
	url(r'^(?i).*CategoryNumbersDelete/(?P<categoryNumbersId>\d+)/$', views.CategoryNumbersDelete),
	
	url(r'^(?i).*EventMassStarts/(?P<competitionId>\d+)/$', views.EventMassStartDisplay),
	url(r'^(?i).*EventMassStartNew/(?P<competitionId>\d+)/$', views.EventMassStartNew),
	url(r'^(?i).*EventMassStartEdit/(?P<eventId>\d+)/$', views.EventMassStartEdit),
	url(r'^(?i).*EventMassStartCrossMgr/(?P<eventId>\d+)/$', views.EventMassStartCrossMgr),
	url(r'^(?i).*EventMassStartDelete/(?P<eventId>\d+)/$', views.EventMassStartDelete),
	
	url(r'^(?i).*WaveNew/(?P<eventMassStartId>\d+)/$', views.WaveNew),
	url(r'^(?i).*WaveEdit/(?P<waveId>\d+)/$', views.WaveEdit),
	url(r'^(?i).*WaveDelete/(?P<waveId>\d+)/$', views.WaveDelete),
	
	url(r'^(?i).*Participants/(?P<competitionId>\d+)/$', views.Participants),
	url(r'^(?i).*ParticipantAdd/(?P<competitionId>\d+)/$', views.ParticipantAdd),
	url(r'^(?i).*ParticipantAddToCompetition/(?P<competitionId>\d+)/(?P<licenseHolderId>\d+)/$', views.ParticipantAddToCompetition),
	url(r'^(?i).*ParticipantAddToCompetitionDifferentCategory/(?P<competitionId>\d+)/(?P<licenseHolderId>\d+)/$',
				views.ParticipantAddToCompetitionDifferentCategory),
	url(r'^(?i).*ParticipantEdit/(?P<participantId>\d+)/$', views.ParticipantEdit),
	url(r'^(?i).*ParticipantDelete/(?P<participantId>\d+)/$', views.ParticipantDelete),
	url(r'^(?i).*ParticipantDoDelete/(?P<participantId>\d+)/$', views.ParticipantDoDelete),
	url(r'^(?i).*LicenseHolderAddConfirm/(?P<competitionId>\d+)/(?P<licenseHolderId>\d+)/$', views.LicenseHolderAddConfirm),
	url(r'^(?i).*LicenseHolderConfirmAddToCompetition/(?P<competitionId>\d+)/(?P<licenseHolderId>\d+)/$', views.LicenseHolderConfirmAddToCompetition),
	
	url(r'^(?i).*ParticipantCategoryChange/(?P<participantId>\d+)/$', views.ParticipantCategoryChange ),
	url(r'^(?i).*ParticipantCategorySelect/(?P<participantId>\d+)/(?P<categoryId>\d+)/$', views.ParticipantCategorySelect ),
	
	url(r'^(?i).*ParticipantRoleChange/(?P<participantId>\d+)/$', views.ParticipantRoleChange ),
	url(r'^(?i).*ParticipantRoleSelect/(?P<participantId>\d+)/(?P<role>\d+)/$', views.ParticipantRoleSelect ),
	
	url(r'^(?i).*ParticipantConfirmedChange/(?P<participantId>\d+)/$', views.ParticipantBooleanChange, {'field':'confirmed'}),
	url(r'^(?i).*ParticipantPreregisteredChange/(?P<participantId>\d+)/$', views.ParticipantBooleanChange, {'field':'preregistered'}),
	url(r'^(?i).*ParticipantPaidChange/(?P<participantId>\d+)/$', views.ParticipantBooleanChange, {'field':'paid'}),
	
	url(r'^(?i).*ParticipantSignatureChange/(?P<participantId>\d+)/$', views.ParticipantSignatureChange ),
	
	url(r'^(?i).*ParticipantTeamChange/(?P<participantId>\d+)/$', views.ParticipantTeamChange ),
	url(r'^(?i).*ParticipantTeamSelect/(?P<participantId>\d+)/(?P<teamId>\d+)/$', views.ParticipantTeamSelect ),
	
	url(r'^(?i).*ParticipantBibChange/(?P<participantId>\d+)/$', views.ParticipantBibChange ),
	url(r'^(?i).*ParticipantBibSelect/(?P<participantId>\d+)/(?P<bib>\d+)/$', views.ParticipantBibSelect ),
	
	url(r'^(?i).*ParticipantTagChange/(?P<participantId>\d+)/$', views.ParticipantTagChange ),
	url(r'^(?i).*ParticipantNoteChange/(?P<participantId>\d+)/$', views.ParticipantNoteChange ),
	
	url(r'^(?i).*LicenseHolders/$', views.LicenseHoldersDisplay),
	url(r'^(?i).*LicenseHolderNew/$', views.LicenseHolderNew),
	url(r'^(?i).*LicenseHolderTagChange/(?P<licenseHolderId>\d+)/$', views.LicenseHolderTagChange),
	url(r'^(?i).*LicenseHolderEdit/(?P<licenseHolderId>\d+)/$', views.LicenseHolderEdit),
	url(r'^(?i).*LicenseHolderDelete/(?P<licenseHolderId>\d+)/$', views.LicenseHolderDelete),
	
	url(r'^(?i).*Teams/$', views.TeamsDisplay),
	url(r'^(?i).*TeamNew/$', views.TeamNew),
	url(r'^(?i).*TeamEdit/(?P<teamId>\d+)/$', views.TeamEdit),
	url(r'^(?i).*TeamDelete/(?P<teamId>\d+)/$', views.TeamDelete),
	
	url(r'^(?i).*CategoryFormats/$', views.CategoryFormatsDisplay),
	url(r'^(?i).*CategoryFormatNew/$', views.CategoryFormatNew),
	url(r'^(?i).*CategoryFormatEdit/(?P<categoryFormatId>\d+)/$', views.CategoryFormatEdit),
	url(r'^(?i).*CategoryFormatCopy/(?P<categoryFormatId>\d+)/$', views.CategoryFormatCopy),
	url(r'^(?i).*CategoryFormatDelete/(?P<categoryFormatId>\d+)/$', views.CategoryFormatDelete),
	
	url(r'^(?i).*CategoryUp/(?P<categoryId>\d+)/$', views.CategoryUp),
	url(r'^(?i).*CategoryDown/(?P<categoryId>\d+)/$', views.CategoryDown),
	
	url(r'^(?i).*CategoryNew/(?P<categoryFormatId>\d+)/$', views.CategoryNew, name='catetory_new'),
	url(r'^(?i).*CategoryEdit/(?P<categoryId>\d+)/$', views.CategoryEdit, name='category_edit'),
	url(r'^(?i).*CategoryDelete/(?P<categoryId>\d+)/$', views.CategoryDelete, name='category_delete'),
	
	url(r'^(?i).*NumberSets/$', views.NumberSetsDisplay),
	url(r'^(?i).*NumberSetNew/$', views.NumberSetNew),
	url(r'^(?i).*NumberSetEdit/(?P<numberSetId>\d+)/$', views.NumberSetEdit),
	url(r'^(?i).*NumberSetDelete/(?P<numberSetId>\d+)/$', views.NumberSetDelete),
	url(r'^(?i).*NumberSetUp/(?P<numberSetId>\d+)/$', views.NumberSetUp),
	url(r'^(?i).*NumberSetDown/(?P<numberSetId>\d+)/$', views.NumberSetDown),
	url(r'^(?i).*NumberSetTop/(?P<numberSetId>\d+)/$', views.NumberSetTop),
	url(r'^(?i).*NumberSetBottom/(?P<numberSetId>\d+)/$', views.NumberSetBottom),
	
	url(r'^(?i).*SeasonsPasses/$', views.SeasonsPassesDisplay),
	url(r'^(?i).*SeasonsPassNew/$', views.SeasonsPassNew),
	url(r'^(?i).*SeasonsPassCopy/(?P<seasonsPassId>\d+)/$', views.SeasonsPassCopy),
	url(r'^(?i).*SeasonsPassEdit/(?P<seasonsPassId>\d+)/$', views.SeasonsPassEdit),
	url(r'^(?i).*SeasonsPassDelete/(?P<seasonsPassId>\d+)/$', views.SeasonsPassDelete),
	url(r'^(?i).*SeasonsPassUp/(?P<seasonsPassId>\d+)/$', views.SeasonsPassUp),
	url(r'^(?i).*SeasonsPassDown/(?P<seasonsPassId>\d+)/$', views.SeasonsPassDown),
	url(r'^(?i).*SeasonsPassTop/(?P<seasonsPassId>\d+)/$', views.SeasonsPassTop),
	url(r'^(?i).*SeasonsPassBottom/(?P<seasonsPassId>\d+)/$', views.SeasonsPassBottom),
	
	url(r'^(?i).*SeasonsPassHolderAdd/(?P<seasonsPassId>\d+)/$', views.SeasonsPassHolderAdd),
	url(r'^(?i).*SeasonsPassHolderRemove/(?P<seasonsPassHolderId>\d+)/$', views.SeasonsPassHolderRemove),
	url(r'^(?i).*SeasonsPassLicenseHolderAdd/(?P<seasonsPassId>\d+)/(?P<licenseHolderId>\d+)/$', views.SeasonsPassLicenseHolderAdd),
	url(r'^(?i).*SeasonsPassLicenseHolderRemove/(?P<seasonsPassId>\d+)/(?P<licenseHolderId>\d+)/$', views.SeasonsPassLicenseHolderRemove),
	
	url(r'^(?i).*RaceClasses/$', views.RaceClassesDisplay),
	url(r'^(?i).*RaceClassNew/$', views.RaceClassNew),
	url(r'^(?i).*RaceClassEdit/(?P<raceClassId>\d+)/$', views.RaceClassEdit),
	url(r'^(?i).*RaceClassDelete/(?P<raceClassId>\d+)/$', views.RaceClassDelete),
	url(r'^(?i).*RaceClassUp/(?P<raceClassId>\d+)/$', views.RaceClassUp),
	url(r'^(?i).*RaceClassDown/(?P<raceClassId>\d+)/$', views.RaceClassDown),
	url(r'^(?i).*RaceClassTop/(?P<raceClassId>\d+)/$', views.RaceClassTop),
	url(r'^(?i).*RaceClassBottom/(?P<raceClassId>\d+)/$', views.RaceClassBottom),
	
	url(r'^(?i).*Disciplines/$', views.DisciplinesDisplay),
	url(r'^(?i).*DisciplineNew/$', views.DisciplineNew),
	url(r'^(?i).*DisciplineEdit/(?P<disciplineId>\d+)/$', views.DisciplineEdit),
	url(r'^(?i).*DisciplineDelete/(?P<disciplineId>\d+)/$', views.DisciplineDelete),
	url(r'^(?i).*DisciplineUp/(?P<disciplineId>\d+)/$', views.DisciplineUp),
	url(r'^(?i).*DisciplineDown/(?P<disciplineId>\d+)/$', views.DisciplineDown),
	url(r'^(?i).*DisciplineTop/(?P<disciplineId>\d+)/$', views.DisciplineTop),
	url(r'^(?i).*DisciplineBottom/(?P<disciplineId>\d+)/$', views.DisciplineBottom),
	
	url(r'^(?i).*SystemInfoEdit/$', views.SystemInfoEdit),
	url(r'^(?i).*QRCode/$', views.QRCode),
	
	url(r'^(?i)login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^(?i).*logout/$', views.Logout),
)