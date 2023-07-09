// Fetch menu data and populate select element
fetch('/menu')
    .then(response => response.json())
    .then(menuData => {
        const dishSelect = document.getElementById('dish-id');
        dishSelect.innerHTML = '';
        menuData.forEach(dish => {
            const option = document.createElement('option');
            option.value = dish.id;
            option.textContent = dish.name;
            dishSelect.appendChild(option);
        });
    })
    .catch(error => console.error('Error:', error));

// Fetch orders data and populate table
fetch('/orders')
    .then(response => response.json())
    .then(ordersData => {
        const ordersTableBody = document.getElementById('orders-table-body');
        ordersTableBody.innerHTML = '';
        ordersData.forEach(order => {
            const row = document.createElement('tr');
            row.innerHTML = `
        <td>${order.id}</td>
        <td>${order.customer_name}</td>
        <td>${order.dish_name}</td>
        <td>${order.order_notes}</td>
        <td>${order.status}</td>
        <td>${order.total_price}</td>
        <td>${order.status === 'received' ? `<a href="/update_status/${order.id}/in progress">Start</a>` : order.status === 'in progress' ? `<a href="/update_status/${order.id}/completed">Complete</a>` : ''}</td>
      `;
            ordersTableBody.appendChild(row);
        });
    })
    .catch(error => console.error('Error:', error));
