function RemoveDesignations(IdRemove) {
          var button_elem = document.getElementById(IdRemove);
          let name_search_element = IdRemove.replace('filter_', '');
          var removeElement = document.getElementById(name_search_element);
          if (removeElement.style.display === "none") {
            removeElement.style.display = "block";
            button_elem.style.backgroundColor  = "";
          } else {
            removeElement.style.display = "none";
            button_elem.style.backgroundColor  = "#A49999"
          }
}
function toggleDropdown() {
          var dropdownMenu = document.querySelector(".dropdown-menu");
          if (dropdownMenu.style.display === "none") {
            dropdownMenu.style.display = "block";
          } else {
            dropdownMenu.style.display = "none";
          }
}
document.addEventListener('DOMContentLoaded', function() {
    const areas = document.querySelectorAll('area[shape="circle"]');
    const highlight = document.getElementById('highlight');
    const imgMap = document.querySelector('.map_img'); // Элемент с классом

    areas.forEach(area => {
        area.addEventListener('mouseover', function() {
            const coords = area.coords.split(',').map(Number);
            const x = coords[0];
            const y = coords[1];
            const radius = coords[2];

            highlight.style.width = radius * 2 + 'px';
            highlight.style.height = radius * 2 + 'px';
            highlight.style.left = ((imgMap.offsetLeft + (x - radius)) * 2) + 'px'; // Положение по X
            highlight.style.top = (imgMap.offsetTop + (y - radius)) + 'px'; // Положение по Y
            highlight.style.display = 'block';
        });

        area.addEventListener('mouseout', function() {
            highlight.style.display = 'none';
        });
    });
});