/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Init Menu
3. InitHeader
4. Init Header Search


******************************/

$(document).ready(function()
{
	"use strict";

	/* 

	1. Vars and Inits

	*/

	var menu = $('.menu');
	var burger = $('.hamburger');
	var menuActive = false;
	var ctrl = new ScrollMagic.Controller();

	initMenu();
	initHeader();
	initHeaderSearch();

	/* 

	2. Init Menu

	*/

	function initMenu()
	{
		if(menu.length)
		{
			if($('.hamburger').length)
			{
				burger.on('click', function()
				{
					if(menuActive)
					{
						closeMenu();
					}
					else
					{
						openMenu();

						$(document).one('click', function cls(e)
						{
							if($(e.target).hasClass('menu_mm'))
							{
								$(document).one('click', cls);
							}
							else
							{
								closeMenu();
							}
						});
					}
				});
			}
		}
	}

	function openMenu()
	{
		menu.addClass('active');
		menuActive = true;
	}

	function closeMenu()
	{
		menu.removeClass('active');
		menuActive = false;
	}

	/* 

	3. InitHeader

	*/

	function initHeader()
	{
		var headerScene = new ScrollMagic.Scene(
		{
			triggerElement: "#header", // point of execution
			triggerHook: 'onLeave', // don't trigger until #pinned-trigger1 hits the top of the viewport
			pushFollowers: false
		})
		.setPin("#header") // the element we want to pin
		.setClassToggle('#header', 'scrolled')
		.addTo(ctrl);
	}

	/* 

	4. Init Header Search

	*/

	function initHeaderSearch()
	{
		if($('.header_search_activation').length)
		{
			var search = $('.header_search_activation');
			var headerSearch = $('.header_search');
			search.on('click', function()
			{
				headerSearch.toggleClass('active');
			});
		}
	}

});