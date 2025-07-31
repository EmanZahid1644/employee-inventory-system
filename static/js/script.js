document.addEventListener('DOMContentLoaded', function() {
    // Real-time dashboard updates
    function updateDashboardStats() {
        fetch('/api/dashboard-stats')
            .then(response => response.json())
            .then(data => {
                document.getElementById('total-employees').textContent = data.total_employees;
                document.getElementById('total-inventory').textContent = data.total_inventory;
                document.getElementById('low-stock').textContent = data.low_stock_count;
            })
            .catch(error => console.error('Error fetching dashboard stats:', error));
    }
    
    // Update stats every 30 seconds
    setInterval(updateDashboardStats, 30000);
    
    // Restock button functionality
    document.querySelectorAll('.btn-restock').forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-id');
            // In a real app, you would make an API call to handle restocking
            alert(`Restocking item with ID: ${itemId}`);
        });
    });
    
    // Notification bell animation
    const notificationBell = document.querySelector('.notification-bell');
    if (notificationBell) {
        notificationBell.addEventListener('click', function() {
            this.classList.add('animate-ring');
            setTimeout(() => {
                this.classList.remove('animate-ring');
            }, 1000);
        });
    }
    
    // Form submission handling
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
            }
        });
    });
    
    // Animation triggers for elements when they come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-slide-up, .animate-fade-in');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };
    
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Trigger on initial load
});

// Add animation for notification bell
const style = document.createElement('style');
style.textContent = `
    @keyframes ring {
        0% { transform: rotate(0); }
        25% { transform: rotate(15deg); }
        50% { transform: rotate(-15deg); }
        75% { transform: rotate(15deg); }
        100% { transform: rotate(0); }
    }
    
    .animate-ring {
        animation: ring 0.5s ease;
    }
`;
document.head.appendChild(style);