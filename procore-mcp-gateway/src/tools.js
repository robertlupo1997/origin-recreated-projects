export const projectsHandler = async (c) => {
  const limit = c.req.query('limit') || '10';
  const offset = c.req.query('offset') || '0';
  
  const projects = [
    {
      id: 'proj-001',
      name: 'Downtown Office Complex',
      status: 'active',
      completion: 0.65,
      manager: 'John Smith',
      budget: 2500000
    },
    {
      id: 'proj-002', 
      name: 'Residential Tower A',
      status: 'planning',
      completion: 0.12,
      manager: 'Sarah Johnson',
      budget: 4200000
    },
    {
      id: 'proj-003',
      name: 'Infrastructure Renovation',
      status: 'active',
      completion: 0.88,
      manager: 'Mike Davis',
      budget: 1800000
    }
  ];

  const startIndex = parseInt(offset);
  const endIndex = startIndex + parseInt(limit);
  
  return c.json({
    projects: projects.slice(startIndex, endIndex),
    total: projects.length,
    limit: parseInt(limit),
    offset: parseInt(offset)
  });
};

export const documentsHandler = async (c) => {
  const projectId = c.req.query('project_id');
  const docType = c.req.query('type') || 'all';
  
  const documents = [
    {
      id: 'doc-001',
      name: 'Blueprint Set A',
      type: 'blueprint',
      project_id: 'proj-001',
      size: 24576000,
      uploaded_at: '2024-01-15T10:30:00Z'
    },
    {
      id: 'doc-002',
      name: 'Safety Report Q4',
      type: 'report',
      project_id: 'proj-001', 
      size: 2048000,
      uploaded_at: '2024-01-20T14:15:00Z'
    },
    {
      id: 'doc-003',
      name: 'Material Specifications',
      type: 'specification',
      project_id: 'proj-002',
      size: 1536000,
      uploaded_at: '2024-01-18T09:45:00Z'
    }
  ];

  let filtered = documents;
  
  if (projectId) {
    filtered = filtered.filter(doc => doc.project_id === projectId);
  }
  
  if (docType !== 'all') {
    filtered = filtered.filter(doc => doc.type === docType);
  }

  return c.json({
    documents: filtered,
    total: filtered.length
  });
};