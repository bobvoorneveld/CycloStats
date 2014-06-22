# -*- coding: utf-8 -*-
stage_response = '''
<html>
<head>
<title>Sports Result</title>
<script type="text/javascript" language="JavaScript">
	<!--
	function Submit2SamePage(oForm) {
		oForm.elements[0].value = 19006;
		oForm.action = 'TheASP.asp';
		oForm.submit();
	};
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakeEventPhase() { this.length=1; return this; }
	EventPhaseID = new MakeEventPhase(); EventPhase = new MakeEventPhase();
	EventPhaseID[0]=891839; EventPhase[0]="Road race";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhase1() { this.length=1; return this; }
	Phase1ID = new MakePhase1(); Phase1 = new MakePhase1();
	Phase1ID[0]=0; Phase1[0]="Final";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhase2() { this.length=1; return this; }
	Phase2ID = new MakePhase2(); Phase2 = new MakePhase2();
	Phase2ID[0]=0; Phase2[0]="";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhase3() { this.length=1; return this; }
	Phase3ID = new MakePhase3(); Phase3 = new MakePhase3();
	Phase3ID[0]=0; Phase3[0]="";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhaseClassification() { this.length=1; return this; }
	PhaseClassificationID = new MakePhaseClassification(); PhaseClassification = new MakePhaseClassification();
	PhaseClassificationID[0]=909930; PhaseClassification[0]="Result";
	// -->
</script>
<script type="text/javascript">

var gpxhr = null;
var gpxhr2 = null;
var gpxhr3 = null;

function processReqChange()
{
	var Vpv = document.getElementById('pri')

	if (gpxhr.readyState == 4)	{
	// 4 = "loaded"
	  if (gpxhr.status == 200)	{
		// 200 = "OK"
		Vpv.innerHTML = gpxhr.responseText;
		}
	  }
}

function processReqChange2()
{
	var Vpv = document.getElementById('seasoncombo')

	if (gpxhr2.readyState == 4)	{
	// 4 = "loaded"
	  if (gpxhr2.status == 200)	{
		// 200 = "OK"
		Vpv.innerHTML = gpxhr2.responseText;
		}
	  }
}

function Dropdown(sportid,competitionid,eventid,genderid,classid,seasonid,eventphaseid,phase1id,containereventid,detail,taalcode,styleid,cache)
{

	if (window.XMLHttpRequest) {
	  gpxhr = new XMLHttpRequest();
	}
	else if (window.ActiveXObject) {
	  gpxhr = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr!=null) {
		gpxhr.onreadystatechange = processReqChange;
		gpxhr.open('post','/asp/redirect/uci.asp?page=dropdown_ranking_phases&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&competitionid='+competitionid+'&eventid='+eventid+'&genderid='+genderid+'&classid='+classid+'&seasonid='+seasonid+'&eventphaseid='+eventphaseid+'&phase1id='+phase1id+'&containereventid='+containereventid+'&detail='+detail+'&cache='+cache);
		gpxhr.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

function fSeasonDropdown(sportid,competitionid,genderid,classid,ranking,detail,taalcode,styleid,cache)
{
	if (window.XMLHttpRequest) {
	  gpxhr2 = new XMLHttpRequest();
	}
	else if (window.ActiveXObject) {
	  gpxhr2 = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr2!=null) {
		gpxhr2.onreadystatechange = processReqChange2;
		if (competitionid == 26328){
			gpxhr2.open('post','/asp/redirect/uci.asp?page=dropdown_season&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+ '&competitionid='+ competitionid +'&genderid='+genderid+'&classid='+classid+'&ranking='+ranking+'&detail='+detail+'&cache='+cache);
		}else{
			gpxhr2.open('post','/asp/redirect/uci.asp?page=dropdown_season&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&genderid='+genderid+'&classid='+classid+'&ranking='+ranking+'&detail='+detail+'&cache='+cache);
		}
		gpxhr2.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

function fSeasonResultDropdown(sportid,competitionid,derivedcompetitionid,phasestatuscode,genderid,classid,ranking,detail,taalcode,styleid,cache)
{


	if (window.XMLHttpRequest) {
	  gpxhr2 = new XMLHttpRequest();
	}
	else if (window.ActiveXObject) {
	  gpxhr2 = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr2!=null) {
		gpxhr2.onreadystatechange = processReqChange2;
		gpxhr2.open('post','/asp/redirect/uci.asp?page=dropdown_season&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+ '&derivedcompetitionid='+derivedcompetitionid+'&phasestatuscode='+phasestatuscode+'&genderid='+genderid+'&classid='+classid+'&ranking='+ranking+'&detail='+detail+'&cache='+cache);
		gpxhr2.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

function processReqChange3()
{
	var Vpv = document.getElementById('personinfo')

	if (gpxhr3.readyState == 4)	{
	// 4 = "loaded"
	  if (gpxhr3.status == 200)	{
		// 200 = "OK"
		Vpv.innerHTML = gpxhr3.responseText;
		}
	  }
}

function PersonRankingInfo(sportid,seasonid,classid,genderid,derivedeventphaseid,derivedcompetitionid,derivedeventid,phase1id,personid,detail,taalcode,styleid,cache)
{
	if (window.XMLHttpRequest) {
	  gpxhr3 = new XMLHttpRequest();

	}
	else if (window.ActiveXObject) {
	  gpxhr3 = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr3!=null) {
		gpxhr3.onreadystatechange = processReqChange3;
		gpxhr3.open("get",'/asp/redirect/uci.asp?page=personrankinginfo&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&seasonid='+seasonid+'&classid='+classid+'&genderid='+genderid+'&derivedeventphaseid='+derivedeventphaseid+'&derivedcompetitionid='+derivedcompetitionid+'&derivedeventid='+derivedeventid+'&phase1id='+phase1id+'&personid='+personid+'&detail='+detail+'&cache='+cache);
		//document.write('/asp/redirect/uci.asp?page=personrankinginfo&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&seasonid='+seasonid+'&classid='+classid+'&genderid='+genderid+'&derivedeventphaseid='+derivedeventphaseid+'&derivedcompetitionid='+derivedcompetitionid+'&derivedeventid='+derivedeventid+'&phase1id='+phase1id+'&personid='+personid+'&detail='+detail+'&cache='+cache);
        //gpxhr3.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        //gpxhr3.setRequestHeader("Content-Type", "text/xml; charset=iso-8859-9");
	    //gpxhr3.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
		gpxhr3.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

</script>

<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<link rel="StyleSheet" href="/css/uci.css" type="text/css">
<script type="text/javascript">
<!--

document.domain='infostradasports.com';

//-->
</script>
<SCRIPT LANGUAGE="JavaScript">
<!--

function scroll2top()
{
	this.window.scrollTo(0,0);
	parent.window.scrollTo(0,0);
}

function loadnav()
{
	slocation = '/asp/navigation_competitions.asp'+window.location.search;
	if (parent.frames['vmenul']) {
		parent.frames['vmenul'].document.location=slocation;
	}
}
// -->
</SCRIPT>
</head>

<body onload="scroll2top();loadnav();document.getElementById('loader').style.display= 'none'">
<img src="/images/icons/loader.gif" id="loader" style="position:absolute; left:50%; top:50%;">


<table  cellspacing="0" cellpadding="0" border=0 width="100%">
<tr><td width="22"><img src="/images/nix.gif" width="22" height="1"></td><td>
<table  cellspacing="0" cellpadding="0" border="0" width="100%"><tr><td valign="top">
<div class="crumblepad">
	<span class="crumblepad_header">Results - Cycling - Road 2014 </span>
	<br/> <br/>
	Men
	<img src="/images/icons/bullet.gif">
	Elite
	<img src="/images/icons/bullet.gif">
	Ronde van Limburg
	(BEL/1.1)
	<br>
	<div class="subtitlered">
		15 Jun 2014 - Road race:
		Tongeren -
		Tongeren
	</div>
</div>


</td><td valign="top" width=120>
<div id="seasoncombo" style="float:right;display:inline;padding-top:5px;">
<script type="text/javascript">
fSeasonDropdown(102, 486, 1, 1, 0, 1, 2, 0, 8)
</script>
</div>
<div style="float:right;padding-top:10px;">

<form name="TheASPform0" action="TheASP.asp" method="get">
<table cellpadding="0" border="0"><tr>
<input name="PageID" type="hidden" value="19006" />
<input name="TaalCode" type="hidden" value="2" />
<input name="StyleID" type="hidden" value="0" />
<input name="Cache" type="hidden" value="8" />
<input name="SportID" type="hidden" value="102" />
<input name="CompetitionID" type="hidden" value="22527" />
<input name="EditionID" type="hidden" value="891420" />
<input name="SeasonID" type="hidden" value="486" />
<input name="EventID" type="hidden" value="10635" />
<input name="GenderID" type="hidden" value="1" />
<input name="ClassID" type="hidden" value="1" />
<input name="PhaseStatusCode" type="hidden" value="262280" />
<input name="EventPhaseID" type="hidden" value="891839" />
<input name="Phase1ID" type="hidden" value="0" />
<input name="Phase2ID" type="hidden" value="0" />
<input name="Phase3ID" type="hidden" value="0" />
<input name="PhaseClassificationID" type="hidden" value="909930" />
<input name="Detail" type="hidden" value="1" />
<input name="Ranking" type="hidden" value="0" />
<input name="DerivedEventPhaseID" type="hidden" value="-1" />
<input name="S00" type="hidden" value="1" /><input name="S01" type="hidden" value="2" /><input name="S02" type="hidden" value="3" /><td></form></div></td></tr></table>
</div>
</td></tr></table><div style="clear:both"></div>
<div class="main_menu_container">
 <div class="content_item_container">
<div class="menu_item_white_border">
	<div class="menu_item_active">
		<div class="menu_item_tekst">
			<a href="/asp/redirect/uci.asp?page=result&SportID=102&CompetitionID=22527&CompetitionCodeInv=1&EditionID=891420&SeasonID=486&EventPhaseID=891839&EventID=10635&ContainerEventID=10635&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&PhaseClassificationID=909930&DerivedEventPhaseID=-1&detail=1&ranking=0">Result</a>
		</div>
	</div>
</div>


</div></div>

<table width="100%" border="0" cellspacing="0" cellpadding="3" class="datatable">
<tr>
	<td class="caption">Rank</td>
	<td class="caption">Name</td>
	<td class="caption">Nat.</td>
	<td class="caption">Team</td>
	<td class="caption" align="center">Age*</td>
	<td class="caption" align="right">Result</td>
	<td class="caption" align="right">PaR</td>
	<td class="caption" align="right">PcR</td>
</tr>
<tr valign="top">
	<td>1 </td>
	<td>Mathieu VAN DER POEL</td>
	<td>NED</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">19</td>
	<td align="right">4:36:27</td>
	<td align="right"><!--80--><span title="UCI Europe Tour Ranking - Individual">80</span></td>
	<td align="right"><!--80--><span title="UCI Europe Tour Ranking - Individual">80</span></td>
</tr>
<tr valign="top">
	<td>2 </td>
	<td>Paul MARTENS</td>
	<td>GER</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">31</td>
	<td align="right">+0</td>
	<td align="right"><!--56--><span title="UCI Europe Tour Ranking - Individual">56</span></td>
	<td align="right"><!--0--><span title="UCI Europe Tour Ranking - Individual">0*</span></td>
</tr>
<tr valign="top">
	<td>3 </td>
	<td>Greg HENDERSON</td>
	<td>NZL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">38</td>
	<td align="right">+0</td>
	<td align="right"><!--32--><span title="UCI Europe Tour Ranking - Individual">32</span></td>
	<td align="right"><!--0--><span title="UCI Europe Tour Ranking - Individual">0*</span></td>
</tr>
<tr valign="top">
	<td>4 </td>
	<td>Oliver NAESEN</td>
	<td>BEL</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!--24--><span title="UCI Europe Tour Ranking - Individual">24</span></td>
	<td align="right"><!--24--><span title="UCI Europe Tour Ranking - Individual">24</span></td>
</tr>
<tr valign="top">
	<td>5 </td>
	<td>Michael VAN STAEYEN</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">26</td>
	<td align="right">+0</td>
	<td align="right"><!--20--><span title="UCI Europe Tour Ranking - Individual">20</span></td>
	<td align="right"><!--20--><span title="UCI Europe Tour Ranking - Individual">20</span></td>
</tr>
<tr valign="top">
	<td>6 </td>
	<td>Jens DEBUSSCHERE</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">25</td>
	<td align="right">+0</td>
	<td align="right"><!--16--><span title="UCI Europe Tour Ranking - Individual">16</span></td>
	<td align="right"><!--0--><span title="UCI Europe Tour Ranking - Individual">0*</span></td>
</tr>
<tr valign="top">
	<td>7 </td>
	<td>Alexander KRIEGER</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!--12--><span title="UCI Europe Tour Ranking - Individual">12</span></td>
	<td align="right"><!--12--><span title="UCI Europe Tour Ranking - Individual">12</span></td>
</tr>
<tr valign="top">
	<td>8 </td>
	<td>Baptiste PLACKAERT</td>
	<td>BEL</td>
	<td><!--RLM--><span title="ROUBAIX LILLE METROPOLE">RLM</span></td>
	<td align="center">26</td>
	<td align="right">+0</td>
	<td align="right"><!--8--><span title="UCI Europe Tour Ranking - Individual">8</span></td>
	<td align="right"><!--8--><span title="UCI Europe Tour Ranking - Individual">8</span></td>
</tr>
<tr valign="top">
	<td>9 </td>
	<td>Omar BERTAZZO</td>
	<td>ITA</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">25</td>
	<td align="right">+0</td>
	<td align="right"><!--7--><span title="UCI Europe Tour Ranking - Individual">7</span></td>
	<td align="right"><!--7--><span title="UCI Europe Tour Ranking - Individual">7</span></td>
</tr>
<tr valign="top">
	<td>10 </td>
	<td>Kenneth VAN BILSEN</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!--6--><span title="UCI Europe Tour Ranking - Individual">6</span></td>
	<td align="right"><!--6--><span title="UCI Europe Tour Ranking - Individual">6</span></td>
</tr>
<tr valign="top">
	<td>11 </td>
	<td>Gianni VERMEERSCH</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">22</td>
	<td align="right">+0</td>
	<td align="right"><!--5--><span title="UCI Europe Tour Ranking - Individual">5</span></td>
	<td align="right"><!--5--><span title="UCI Europe Tour Ranking - Individual">5</span></td>
</tr>
<tr valign="top">
	<td>12 </td>
	<td>Maxime VANTOMME</td>
	<td>BEL</td>
	<td><!--RLM--><span title="ROUBAIX LILLE METROPOLE">RLM</span></td>
	<td align="center">28</td>
	<td align="right">+0</td>
	<td align="right"><!--3--><span title="UCI Europe Tour Ranking - Individual">3</span></td>
	<td align="right"><!--3--><span title="UCI Europe Tour Ranking - Individual">3</span></td>
</tr>
<tr valign="top">
	<td>13 </td>
	<td>Tijmen EISING</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>14 </td>
	<td>Mike TEUNISSEN</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">22</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>15 </td>
	<td>Tom VAN ASBROECK</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>16 </td>
	<td>Coen VERMELTFOORT</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">26</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>17 </td>
	<td>Roy JANS</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>18 </td>
	<td>Antoine DEMOITIE</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>19 </td>
	<td>Kevin PEETERS</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">27</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>20 </td>
	<td>Kevin FEIEREISEN</td>
	<td>LUX</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">22</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>21 </td>
	<td>Johnny HOOGERLAND</td>
	<td>NED</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">31</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>22 </td>
	<td>Olivier PARDINI</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">29</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>23 </td>
	<td>Marcel MEISEN</td>
	<td>GER</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">25</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>24 </td>
	<td>Nicolas VEREECKEN</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>25 </td>
	<td>Marco MINNAARD</td>
	<td>NED</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">25</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>26 </td>
	<td>Jarno GMELICH</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">25</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>27 </td>
	<td>Gaetan BILLE</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">26</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>28 </td>
	<td>Jérôme GILBERT</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">30</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>29 </td>
	<td>Robbert DE GREEF</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>30 </td>
	<td>Andrea ZORDAN</td>
	<td>ITA</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">22</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>31 </td>
	<td>Etienne VAN EMPEL</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">20</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>32 </td>
	<td>Daan HOEYBERGHS</td>
	<td>BEL</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">20</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>33 </td>
	<td>Kevin VAN MELSEN</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">27</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>34 </td>
	<td>Jeroen MEIJERS</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">21</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>35 </td>
	<td>Marco ZANOTTI</td>
	<td>ITA</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">26</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>36 </td>
	<td>Julien STASSEN</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">26</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>37 </td>
	<td>Dennis COENEN</td>
	<td>BEL</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>38 </td>
	<td>Yoeri HAVIK</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>39 </td>
	<td>Sam LENNERTZ</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">24</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>40 </td>
	<td>Martin BINA</td>
	<td>CZE</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">31</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>41 </td>
	<td>Kenny GOOSSENS</td>
	<td>BEL</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>42 </td>
	<td>David VAN DER POEL</td>
	<td>NED</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">22</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>43 </td>
	<td>Marco KÖNIG</td>
	<td>GER</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">19</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>44 </td>
	<td>Vinnie BRAET</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>45 </td>
	<td>Nikodemus HOLLER</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">23</td>
	<td align="right">+0</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>46 </td>
	<td>Wout VAN AERT</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">20</td>
	<td align="right">+8</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>47 </td>
	<td>Kevin PAUWELS</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">30</td>
	<td align="right">+8</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>48 </td>
	<td>Wietse BOSMANS</td>
	<td>BEL</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">23</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>49 </td>
	<td>Peter KONING</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">24</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>50 </td>
	<td>Thijs VAN AMERONGEN</td>
	<td>NED</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">28</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>51 </td>
	<td>Laurens SWEECK</td>
	<td>BEL</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">21</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>52 </td>
	<td>Vincent BAESTAENS</td>
	<td>BEL</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">25</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>53 </td>
	<td>Kobus HEREIJGERS</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">25</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>54 </td>
	<td>Lennard HOFSTEDE</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">20</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>55 </td>
	<td>André LOOIJ</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">19</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>56 </td>
	<td>Floris SMEYERS</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">24</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>57 </td>
	<td>Lubomir PETRUS</td>
	<td>CZE</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">24</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>58 </td>
	<td>Jim AERNOUTS</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">25</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>59 </td>
	<td>Michael GOOLAERTS</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">20</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>60 </td>
	<td>Bart WELLENS</td>
	<td>BEL</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">36</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>61 </td>
	<td>Niels WUBBEN</td>
	<td>NED</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">26</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>62 </td>
	<td>Kevin CALLEBAUT</td>
	<td>BEL</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">23</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>63 </td>
	<td>Corne VAN KESSEL</td>
	<td>NED</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">23</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>64 </td>
	<td>Remco BROERS</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">26</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>65 </td>
	<td>Gert-Jan BOSMAN</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">22</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>66 </td>
	<td>Ivar SLIK</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">21</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>67 </td>
	<td>Bram NOLTEN</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">23</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>68 </td>
	<td>Quentin JAUREGUI</td>
	<td>FRA</td>
	<td><!--RLM--><span title="ROUBAIX LILLE METROPOLE">RLM</span></td>
	<td align="center">20</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>69 </td>
	<td>Sébastien DELFOSSE</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">32</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>70 </td>
	<td>Tino THÖMEL</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">26</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>71 </td>
	<td>Twan CASTELIJNS</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">25</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>72 </td>
	<td>Rob RUIJGH</td>
	<td>NED</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">28</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>73 </td>
	<td>Mathias VAN HOLDERBEKE</td>
	<td>BEL</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">22</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>74 </td>
	<td>Ike GROEN</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">22</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>75 </td>
	<td>Jarl SALOMEIN</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">25</td>
	<td align="right">+10</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>76 </td>
	<td>Philipp WALSLEBEN</td>
	<td>GER</td>
	<td><!--BKP--><span title="BKCP - POWERPLUS">BKP</span></td>
	<td align="center">27</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>77 </td>
	<td>Frédéric AMORISON</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">36</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>78 </td>
	<td>Martijn TUSVELD</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">21</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>79 </td>
	<td>Lars Ytting BAK</td>
	<td>DEN</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">34</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>80 </td>
	<td>Wesley KREDER</td>
	<td>NED</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">24</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>81 </td>
	<td>Frederik BACKAERT</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">24</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>82 </td>
	<td>Peter SCHULTING</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">27</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>83 </td>
	<td>Marcel SIEBERG</td>
	<td>GER</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">32</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>84 </td>
	<td>Kenny Robert VAN HUMMEL</td>
	<td>NED</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">32</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>85 </td>
	<td>Bertjan LINDEMAN</td>
	<td>NED</td>
	<td><!--RDT--><span title="RABOBANK DEVELOPMENT TEAM">RDT</span></td>
	<td align="center">25</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>86 </td>
	<td>Kevin HULSMANS</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">36</td>
	<td align="right">+29</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>87 </td>
	<td>Frederique ROBERT</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">25</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>88 </td>
	<td>Jasper OCKELOEN</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">24</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>89 </td>
	<td>Jesper ASSELMAN</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">24</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>90 </td>
	<td>Jetse BOL</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">25</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>91 </td>
	<td>Remco TE BRAKE</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">26</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>92 </td>
	<td>Sander HELVEN</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">24</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>93 </td>
	<td>Olivier CHEVALIER</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">24</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>94 </td>
	<td>Theo BOS</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">31</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>95 </td>
	<td>Thomas SPRENGERS</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">24</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>96 </td>
	<td>Tom MEEUSEN</td>
	<td>BEL</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">26</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>97 </td>
	<td>Nico SIJMENS</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">36</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>98 </td>
	<td>Graeme BROWN</td>
	<td>AUS</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">35</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>99 </td>
	<td>Julien DUVAL</td>
	<td>FRA</td>
	<td><!--RLM--><span title="ROUBAIX LILLE METROPOLE">RLM</span></td>
	<td align="center">24</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>100 </td>
	<td>Radomir SIMUNEK</td>
	<td>CZE</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">31</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>101 </td>
	<td>Sean DE BIE</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">23</td>
	<td align="right">+47</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>102 </td>
	<td>Robin STENUIT</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">24</td>
	<td align="right">+1:20</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>103 </td>
	<td>Marco BANDIERA</td>
	<td>ITA</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">30</td>
	<td align="right">+1:34</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>104 </td>
	<td>Tiziano DALL'ANTONIA</td>
	<td>ITA</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">31</td>
	<td align="right">+1:34</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>105 </td>
	<td>Marco FRAPPORTI</td>
	<td>ITA</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">29</td>
	<td align="right">+1:34</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>106 </td>
	<td>Nicola TESTI</td>
	<td>ITA</td>
	<td><!--AND--><span title="ANDRONI GIOCATTOLI - VENEZUELA">AND</span></td>
	<td align="center">24</td>
	<td align="right">+1:34</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>107 </td>
	<td>Tim WELLENS</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">23</td>
	<td align="right">+1:59</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>108 </td>
	<td>Stijn STEELS</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">25</td>
	<td align="right">+2:11</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>109 </td>
	<td>Robert WAGNER</td>
	<td>GER</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">31</td>
	<td align="right">+3:53</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td>110 </td>
	<td>Jos VAN EMDEN</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">29</td>
	<td align="right">+3:53</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Jonathan DUFRASNE</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Florent MOTTET</td>
	<td>BEL</td>
	<td><!--WBC--><span title="WALLONIE - BRUXELLES">WBC</span></td>
	<td align="center">23</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Boris VALLEE</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Rick FLENS</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">31</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Dennis VAN WINDEN</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Tim DECLERCQ</td>
	<td>BEL</td>
	<td><!--TSV--><span title="TOPSPORT VLAANDEREN - BALOISE">TSV</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Dieter VANTHOURENHOUT</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Michael VANTHOURENHOUT</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Toon AERTS</td>
	<td>BEL</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Ben BOETS</td>
	<td>BEL</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">19</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Quinten HERMANS</td>
	<td>BEL</td>
	<td><!--TFC--><span title="TELENET - FIDEA">TFC</span></td>
	<td align="center">19</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Kevin CANT</td>
	<td>BEL</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Diether SWEECK</td>
	<td>BEL</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Hendrik SWEECK</td>
	<td>BEL</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">22</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Julien TARAMARCAZ</td>
	<td>SUI</td>
	<td><!--KWS--><span title="KWADRO - STANNAH">KWS</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Piero BAFFI</td>
	<td>ITA</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Alex KIRSCH</td>
	<td>LUX</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">22</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Pit SCHLECHTER</td>
	<td>LUX</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Tom THILL</td>
	<td>LUX</td>
	<td><!--LDT--><span title="LEOPARD DEVELOPMENT TEAM">LDT</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Nick WYNANTS</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">22</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Sander CORDEEL</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Rob PEETERS</td>
	<td>BEL</td>
	<td><!--VGS--><span title="VASTGOEDSERVICE - GOLDEN PALACE CONTINENTAL TEAM">VGS</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Timothy DUPONT</td>
	<td>BEL</td>
	<td><!--RLM--><span title="ROUBAIX LILLE METROPOLE">RLM</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Umberto ATZORI</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Jasper BOVENHUIS</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">23</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>René HOOGHIEMSTER</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">28</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Arno VAN DER ZWET</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">28</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Bart VAN HAAREN</td>
	<td>NED</td>
	<td><!--KOG--><span title="KOGA CYCLING TEAM">KOG</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Jack CUMMINGS</td>
	<td>AUS</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">20</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Kai KAUTZ</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Georg LOEF</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">20</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Max WALSLEBEN</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Christopher MUCHE</td>
	<td>GER</td>
	<td><!--SGT--><span title="TEAM STUTTGART">SGT</span></td>
	<td align="center">22</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Jérémy BURTON</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Niels VANDYCK</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Louis CONVENS</td>
	<td>BEL</td>
	<td><!--WIL--><span title="VERANDAS WILLEMS">WIL</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Dries HOLLANDERS</td>
	<td>BEL</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">28</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Dennis SMIT</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">33</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Brian VAN GOETHEM</td>
	<td>NED</td>
	<td><!--MET--><span title="METEC - TKH CONTINENTAL CYCLINGTEAM">MET</span></td>
	<td align="center">23</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Huub DUYN</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Dylan GROENEWEGEN</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Sjoerd KOUWENHOVEN</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Ronan VAN ZANDBEEK</td>
	<td>NED</td>
	<td><!--RIJ--><span title="CYCLINGTEAM DE RIJKE">RIJ</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Marco HOEKSTRA</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Lars HORRING</td>
	<td>NED</td>
	<td><!--PVC--><span title="PARKHOTEL VALKENBURG CONTINENTAL CYCLING TEAM">PVC</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Bjorn DE DECKER</td>
	<td>BEL</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Martynas MANIUSIS</td>
	<td>LTU</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Niels SCHITTECATTE</td>
	<td>BEL</td>
	<td><!--CIB--><span title="CIBEL">CIB</span></td>
	<td align="center">22</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Tom ARMSTRONG</td>
	<td>GBR</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">20</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Jonathan BARATTO</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">23</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Julien DESCHESNE</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">23</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Guillaume HAAG</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Glenn VANDEMAELE</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Maxime VEKEMAN</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Kévin THOME</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DNF</td>
	<td>Andrew YDENS</td>
	<td>BEL</td>
	<td><!--PCW--><span title="T.PALM - PÔLE CONTINENTAL WALLON">PCW</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
<tr valign="top">
	<td> DSQ</td>
	<td>Tim MERLIER</td>
	<td>BEL</td>
	<td><!--SUN--><span title="SUNWEB - NAPOLEON GAMES CYCLING TEAM">SUN</span></td>
	<td align="center">22</td>
	<td align="right">&nbsp;</td>
	<td align="right"><!----><span title=""></span></td>
	<td align="right"><!----><span title=""></span></td>
</tr>
</table>
<table width="98%" border="0" cellspacing="0" cellpadding="2" class="datatablelegend">
<tr valign="top"><td colspan="2">Age*:&nbsp;according to UCI Regulations, &nbsp;PaR:&nbsp;UCI points according to Rank, &nbsp;PcR:&nbsp;UCI points calculated in Ranking:br>
* Not allowed to receive points<br>
** Not amongst best results<br></td></tr>
</table>
</td><td width="5"><img src="/images/nix.gif" width="5" height="1"></td></tr></table>
<br /><img src="/images/libs/nix.gif" width=1  height=5 border=0>

</font>
</body>
</html>
'''
