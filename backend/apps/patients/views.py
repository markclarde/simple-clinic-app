from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from apps.accounts.models import User

class CreatePatientProfileView(generics.CreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        if user.role == "doctor":
            return Response({"detail": "Doctors are not allowed to create patient profiles."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)  # This is now customized below
        return Response({
            "message": "Patient profile created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # ✅ This sets the authenticated user as the owner
        serializer.save(user=self.request.user)
